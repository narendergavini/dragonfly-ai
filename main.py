from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
import uuid
import json
from prompt import system_prompt, procrastination_DF_metadata
import re
from docx import Document

# Try to import streamlit for secrets handling (for cloud deployment)
try:
    import streamlit as st
    # Use Streamlit secrets if available (for cloud deployment)
    if hasattr(st, 'secrets') and 'secrets' in st.secrets:
        OPENAI_API_KEY = st.secrets["secrets"]["OPENAI_API_KEY"]
        LANGCHAIN_API_KEY = st.secrets["secrets"]["LANGCHAIN_API_KEY"]
        LANGCHAIN_PROJECT = st.secrets["secrets"]["LANGCHAIN_PROJECT"]
    else:
        # Fallback to environment variables
        load_dotenv()
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
        LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "dragonfly")
except ImportError:
    # If streamlit is not available, use environment variables
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
    LANGCHAIN_PROJECT = os.getenv("LANGCHAIN_PROJECT", "dragonfly")

os.environ["LANGCHAIN_TRACING_V2"] = "true"
if LANGCHAIN_API_KEY:
    os.environ["LANGCHAIN_API_KEY"] = LANGCHAIN_API_KEY
if LANGCHAIN_PROJECT:
    os.environ["LANGCHAIN_PROJECT"] = LANGCHAIN_PROJECT


# Function to extract script content by title from .docx file
def extract_script_by_title(filepath, title):
    try:
        doc = Document(filepath)
        collecting = False
        content = []
        for para in doc.paragraphs:
            if collecting:
                # Stop at the next known title
                if any(v["title"] in para.text for v in procrastination_DF_metadata.values()):
                    break
                content.append(para.text)
            elif title in para.text:
                collecting = True
        return "\n".join(content)
    except Exception as e:
        print(f"Error extracting script by title: {e}")
        return None


# dragonfly project setup
class StudyBuddy:
    def __init__(self, knowledge_base_path=None, base_directory="cleaned_data"):
        self.model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
        self.memory = MemorySaver()  # Enable memory for conversation history
        self.thread_id = str(uuid.uuid4())  # Generate unique thread ID
        self.knowledge_base_path = knowledge_base_path
        self.base_directory = base_directory  # Directory where txt files are stored
        self.knowledge_base = None
        self.category_cache = {}  # Cache for processed category content
        self.config = {
            "configurable": {"thread_id": self.thread_id},
            "run_id": str(uuid.uuid4()),
            "run_name": f"study-buddy-{self.thread_id}",
        }

    def auto_detect_knowledge_base_path(self, category):
        """Auto-detect knowledge base file path based on category name"""
        try:
            # First, try exact match with .txt extension in base directory
            txt_path = os.path.join(self.base_directory, f"{category}.txt")
            if os.path.exists(txt_path):
                return txt_path
            
            # If not found, check if there's a .docx file with category info in the base directory
            docx_path = os.path.join(self.base_directory, "Procrastination DF SCRIPTS.docx")
            if os.path.exists(docx_path):
                # Check if category exists in docx metadata
                for metadata in procrastination_DF_metadata.values():
                    if category in metadata["title"]:
                        return docx_path
            
            # If still not found, print error and return None
            print(f"❌ Category '{category}' not found in knowledge base!")
            return None
        except Exception as e:
            print(f"Error auto-detecting knowledge base path: {e}")
            return None

    def load_knowledge_base_for_category(self, category):
        """Load knowledge base dynamically based on category"""
        try:
            # Check if knowledge base is already loaded for this category
            if self.knowledge_base is not None:
                return True
                
            # Auto-detect the correct file path
            detected_path = self.auto_detect_knowledge_base_path(category)
            if detected_path is None:
                return False
            
            # Set the knowledge base path and load it
            self.knowledge_base_path = detected_path
            return self.load_knowledge_base()
            
        except Exception as e:
            print(f"Error loading knowledge base for category '{category}': {e}")
            return False

    # Load knowledge base
    def load_knowledge_base(self):
        """Load the knowledge base - TXT file or recognize .docx file (no pre-caching)"""
        try:
            if self.knowledge_base_path is None:
                print("No knowledge base path provided")
                return False
                
            if self.knowledge_base_path.endswith(".txt"):
                # Load TXT file into memory (but don't cache categories yet)
                with open(self.knowledge_base_path, "r", encoding="utf-8") as f:
                    self.knowledge_base = f.read()
                print(f"TXT knowledge base loaded from {self.knowledge_base_path}")
                return True
                
            elif self.knowledge_base_path.endswith(".docx"):
                # For .docx files, just verify the file exists
                if os.path.exists(self.knowledge_base_path):
                    print(f"Word document recognized: {self.knowledge_base_path}")
                    print("Content will be extracted and cached on-demand")
                    self.knowledge_base = "docx_file"  # Flag to indicate docx mode
                    return True
                else:
                    raise FileNotFoundError(f"Word document not found: {self.knowledge_base_path}")
            else:
                raise ValueError(f"Unsupported file format. Only .txt and .docx files are supported: {self.knowledge_base_path}")
            
        except FileNotFoundError:
            print(f"Knowledge base file not found: {self.knowledge_base_path}")
            self.knowledge_base = ""
            return False
        except Exception as e:
            print(f"Error reading file: {e}")
            self.knowledge_base = ""
            return False

    # Get available categories
    def get_available_categories(self):
        """Get a list of available categories in the knowledge base"""
        try:
            if self.knowledge_base == "docx_file":
                # For .docx files, return the script titles from metadata
                return [metadata["title"] for metadata in procrastination_DF_metadata.values()]
            elif isinstance(self.knowledge_base, str):
                # For TXT files, extract filename as category
                category_name = os.path.basename(self.knowledge_base_path).replace('.txt', '')
                return [category_name]
            else:
                # For cached categories
                return list(self.category_cache.keys())
        except Exception as e:
            print(f"Error getting available categories: {e}")
            return []

    # Get content for a specific category (lazy loading)
    def get_category_content(self, category):
        """Get content for a specific category (lazy loading - cache only when requested)"""
        try:
            # Check if already cached
            if category in self.category_cache:
                return self.category_cache[category]
            
            # Not cached yet - load and cache the specific category
            print(f"Loading and caching content for category: {category}")
            
            if self.knowledge_base == "docx_file":
                # Extract from .docx file
                content = extract_script_by_title(self.knowledge_base_path, category)
                if content and not (content.startswith("Error") or content is None):
                    self.category_cache[category] = content
                    print(f"Successfully cached DOCX content for: {category}")
                    return content
                else:
                    print(f"Failed to extract content for category: {category}")
                    return None

            elif isinstance(self.knowledge_base, str):
                # For TXT files, the entire content is the category content
                self.category_cache[category] = self.knowledge_base
                print(f"Successfully cached TXT content for: {category}")
                return self.knowledge_base
            else:
                available_categories = self.get_available_categories()
                print(f"Category '{category}' not found. Available categories: {available_categories[:5]}...")  # Show first 5
                return None
            
        except Exception as e:
            print(f"Error retrieving category content: {e}")
            return None


    def prepare_prompt_create_agent(self, category=None):
        """Prepare the prompt template and create the agent executor"""
        try:
            # If category is provided, include its content in system prompt
            if category:
                category_content = self.get_category_content(category)
                if category_content:
                    enhanced_system_prompt = f"""{system_prompt}
                KNOWLEDGE BASE CONTENT FOR {category.upper()}:
                === CONTENT START ===
                {category_content}
                === CONTENT END ===
                Use the above content to answer questions about {category}. This content is available for the entire conversation session."""
                else:
                    enhanced_system_prompt = system_prompt
            else:
                enhanced_system_prompt = system_prompt
            
            # Create a comprehensive system prompt based on prompt.py instructions
            self.prompt_template = ChatPromptTemplate.from_messages([
                ("system", enhanced_system_prompt),
                MessagesPlaceholder(variable_name="messages"),
            ])
            
            self.agent_executor = create_react_agent(
                self.model, 
                tools=[],  # No tools needed
                checkpointer=self.memory,
                prompt=self.prompt_template,
            )
        except Exception as e:
            print(f"Error preparing prompt and creating agent: {e}")
            self.agent_executor = None
    
    def get_response(self, category, query):
        """Get response based on category-specific content and user query with memory"""
        try:
            # Check if agent is prepared for this category
            if not hasattr(self, f'_agent_prepared_{category}'):
                # Prepare agent with category-specific content in system prompt
                self.prepare_prompt_create_agent(category)
                setattr(self, f'_agent_prepared_{category}', True)
            
            # Simply send the user query - content is already in system prompt
            response = self.agent_executor.invoke(
                {"messages": [HumanMessage(content=query)]},
                config=self.config,
            )
            return response["messages"][-1].content
        except Exception as e:
            print(f"Error getting response: {e}")
            return "Sorry! I'm unable to answer this based on the provided content."
    
    # Simple interface for asking questions in a specific category
    def ask_query(self, category, query):
        """Simple interface for asking questions in a specific category"""
        return self.get_response(category, query)



