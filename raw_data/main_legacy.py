from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
import uuid
import json
from prompt import system_prompt


load_dotenv() 


os.environ["LANGCHAIN_TRACING_V2"] = "true"
LANGCHAIN_API_KEY = os.getenv("LANGCHAIN_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "DefaultProject")


# dragonfly project setup
class StudyBuddy:
    def __init__(self, knowledge_base_path=None):
        self.model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
        self.memory = MemorySaver()  # Enable memory for conversation history
        self.thread_id = str(uuid.uuid4())  # Generate unique thread ID
        self.knowledge_base_path = knowledge_base_path
        self.knowledge_base = None
        self.category_cache = {}  # Cache for processed category content
        self.config = {
            "configurable": {"thread_id": self.thread_id},
            "run_id": str(uuid.uuid4()),
            "run_name": f"study-buddy-{self.thread_id}",
        }

    def load_knowledge_base(self):
        """Load the cleaned knowledge base JSON file and cache all category content"""
        try:
            with open(self.knowledge_base_path, "r") as f:
                self.knowledge_base = json.load(f)
            
            # Pre-process and cache all category content
            self._cache_all_categories()
            print(f"Knowledge base loaded with {len(self.category_cache)} categories cached")
            
        except FileNotFoundError:
            print(f"Knowledge base file not found: {self.knowledge_base_path}")
            self.knowledge_base = {}
        except json.JSONDecodeError:
            print(f"Invalid JSON format in: {self.knowledge_base_path}")
            self.knowledge_base = {}
    
    def _cache_all_categories(self):
        """Pre-process and cache all category content for faster retrieval"""
        if not self.knowledge_base:
            return
            
        for category, content in self.knowledge_base.items():
            # Convert list content to readable text and cache it
            if isinstance(content, list):
                self.category_cache[category] = "\n".join(content)
            else:
                self.category_cache[category] = str(content)


    def get_available_categories(self):
        """Get a list of available categories in the knowledge base"""
        try:
            return list(self.category_cache.keys())
        except Exception as e:
            print(f"Error getting available categories: {e}")
            return []
    
    def get_cache_info(self):
        """Get information about the cached categories"""
        try:
            cache_info = {}
            for category, content in self.category_cache.items():
                cache_info[category] = {
                    'content_length': len(content),
                    'lines_count': len(content.split('\n')) if content else 0
                }
            return cache_info
        except Exception as e:
            print(f"Error getting cache info: {e}")
            return {}

    def get_category_content(self, category):
        """Get cached content for a specific category"""
        try:
            if category not in self.category_cache:
                available_categories = self.get_available_categories()
                print(f"Category '{category}' not found. Available categories: {available_categories}")
                return None
            
            # Return cached content (no processing needed)
            print(f"Retrieving cached content for category: {category}")
            return self.category_cache[category]
            
        except Exception as e:
            print(f"Error retrieving category content: {e}")
            return None


    def prepare_prompt_create_agent(self):
        """Prepare the prompt template and create the agent executor"""
        try:
            # Create a comprehensive system prompt based on prompt.py instructions
            self.prompt_template = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
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
            # Get content for the specified category
            category_content = self.get_category_content(category)
            
            if category_content is None:
                return f"Sorry, I couldn't find information for the category '{category}'."
            
            # Create a context-aware message that provides the category content and user query
            # This allows the agent to use both the content and maintain conversation memory
            context_message = f"""Here is the {category} knowledge base content to help answer the user's question:
                === {category.upper()} CONTENT ===
                {category_content}
                === END CONTENT ===
                User's question: {query}
                Please use the above content along with our conversation history to provide a helpful response."""
            
            # Get response from the agent with memory
            response = self.agent_executor.invoke(
                {"messages": [HumanMessage(content=context_message)]},
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


# Main execution
def main(knowledge_base_path, category=None, query=None):
    """Main function to initialize StudyBuddy and process a query."""
    try:
        if category is None or query is None:
            print("Please provide both category and query parameters.")
            return None
        
        # Initialize StudyBuddy with knowledge base path
        study_buddy = StudyBuddy(knowledge_base_path=knowledge_base_path)
        
        # Load the knowledge base (this caches all categories)
        study_buddy.load_knowledge_base()
        
        # Prepare the agent
        study_buddy.prepare_prompt_create_agent()
        
        # Example usage with specified category
        response = study_buddy.ask_query(category, query)
        print("\n&&&&&&&&&&&&&&&&&&&&& START &&&&&&&&&&&&&&&&&&&& ")
        print(f"Category: {category}")
        print(f"Query: {query}")
        print(f"Response: {response}")
        print("&&&&&&&&&&&&&&&&&&&& END &&&&&&&&&&&&&&&&&&&&\n\n")
        return response 
    except Exception as e:
        print(f"Error in main execution: {e}")
        return None



######################################################################################################################
if __name__ == "__main__":
    knowledge_base_path = "cleaned_knowledge_base.json"
    category="StudySkills",
    query="What is study skills?"
    results = main(
        knowledge_base_path=knowledge_base_path,
        category=category,
        query=query)


    # category="None"
    # # Initialize StudyBuddy with knowledge base path
    # study_buddy = StudyBuddy(knowledge_base_path=knowledge_base_path)
    # # Load the knowledge base (this caches all categories)
    # study_buddy.load_knowledge_base()
    # # Prepare the agent
    # study_buddy.prepare_prompt_create_agent()
    # while True:
    #     query = input("Enter your query (or type 'exit' to quit): ")
    #     if query.lower() == 'exit':
    #         break
    #     results = study_buddy.ask_query(category, query)
    #     print("Results:", results)


