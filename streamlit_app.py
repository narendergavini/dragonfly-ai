import streamlit as st
import os
from main import StudyBuddy

# Check for API keys
try:
    # Check if API keys are available (either from secrets or environment)
    if hasattr(st, 'secrets') and 'secrets' in st.secrets:
        openai_key = st.secrets["secrets"].get("OPENAI_API_KEY")
        langchain_key = st.secrets["secrets"].get("LANGCHAIN_API_KEY")
    else:
        openai_key = os.getenv("OPENAI_API_KEY")
        langchain_key = os.getenv("LANGCHAIN_API_KEY")
    
    if not openai_key:
        st.error("⚠️ OpenAI API key not found. Please configure your secrets.")
        st.stop()
        
except Exception as e:
    st.error(f"⚠️ Configuration error: {str(e)}")
    st.stop()

# Streamlit page configuration
st.set_page_config(page_title="Dragonfly", page_icon=":robot_face:")

# Title of the app
st.title("Dragonfly 🤖")

# Initialize session state variables if not already present
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
    # Add a default welcome message
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": "Welcome to Dragonfly AI"
    })
if 'current_user_query' not in st.session_state:
    st.session_state.current_user_query = ""
if 'current_response' not in st.session_state:
    st.session_state.current_response = ""
if 'study_buddy' not in st.session_state:
    st.session_state.study_buddy = None
if 'current_category' not in st.session_state:
    st.session_state.current_category = None
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = None

# Function to initialize or switch StudyBuddy for a category
def get_study_buddy(category):
    """Get or create StudyBuddy instance for the category"""
    # If category changed or no study_buddy exists, create a new one
    if (st.session_state.current_category != category or 
        st.session_state.study_buddy is None):
        
        try:
            study_buddy = StudyBuddy(base_directory="cleaned_data")
            
            if not study_buddy.load_knowledge_base_for_category(category):
                return None, f"Sorry, I couldn't find a knowledge base for category '{category}'."
            
            study_buddy.prepare_prompt_create_agent(category)
            
            # Update session state
            st.session_state.study_buddy = study_buddy
            st.session_state.current_category = category
            
            return study_buddy, None
            
        except Exception as e:
            return None, f"Error initializing for category '{category}': {e}"
    
    return st.session_state.study_buddy, None

# Function to get response using persistent StudyBuddy
def get_ai_response(category, query):
    """Get AI response using persistent StudyBuddy instance"""
    study_buddy, error = get_study_buddy(category)
    
    if error:
        return error
    
    try:
        return study_buddy.ask_query(category, query)
    except Exception as e:
        return f"Sorry, I encountered an error: {str(e)}"

# Use st.empty() to control where the chat history and new responses appear
chat_placeholder = st.empty()

# Function to display chat history
def display_chat_history():
    with chat_placeholder.container():
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                col1, col2 = st.columns([1, 5])
                with col2:
                    st.chat_message("user").write(message["content"])
            elif message["role"] == "assistant":
                col1, col2 = st.columns([5, 1])
                with col1:
                    st.chat_message("assistant").write(message["content"])

# Display the chat history
display_chat_history()

# User input section at side bar only for category selection
st.sidebar.header("⚙️ Settings")
# All available categories (hardcoded)
# Text file categories
txt_categories = [
    "StudySkills",
    "ProcrastinationHack", 
    "TimeManagement",
    "CrunchTime",
    "Introduction"
]

# Get DOCX categories dynamically from the StudyBuddy class
try:
    from prompt import procrastination_DF_metadata
    docx_categories = [metadata["title"] for metadata in procrastination_DF_metadata.values()]
except Exception as e:
    # Fallback to hardcoded list if there's an issue
    docx_categories = [
        "Conquering Fear-Based Procrastination (22-Minute Session)",
        "Conquering Rebellion Procrastination (22-Minute Session)",
        "Conquering Deadline Procrastination (22-Minute Session)",
        "Conquering Decision Procrastination (22-Minute Session)",
        "Conquering Task Overwhelm Procrastination (22-Minute Session)",
        "Conquering Lack of Interest Procrastination (22-Minute Session)",
        "Conquering Perfectionism Procrastination (22-Minute Session)",
        "Conquering Decision Paralysis (22-Minute Session)",
        "Conquering Perfectionist Procrastination (22-Minute Session)",
        "Conquering Avoidant Procrastination (22-Minute Session)",
        "Conquering Decision Paralysis Procrastination (22-Minute Session)",
        "Conquering Deadline Adrenaline Procrastination (22-Minute Session)",
        "Conquering Distraction Procrastination (22-Minute Session)",
        "Conquering Productive Procrastination (22-Minute Session)",
        "Conquering Fear of Failure Procrastination (22-Minute Session)",
        "Conquering Energy Depletion Procrastination (22-Minute Session)",
        "Conquering Unclear Goals Procrastination (22-Minute Session)",
        "Conquering Skill Gap Procrastination (22-Minute Session)",
        "Conquering Pleasure-Seeking Procrastination (22-Minute Session)",
        "Conquering Arousal Procrastination (22-Minute Session)",
        "Conquering Bedtime Procrastination (22-Minute Session)"
    ]

# Combine all categories
all_categories = txt_categories + docx_categories

# Category selection dropdown
category = st.sidebar.selectbox(
    "📚 Select Study Category:",
    options=all_categories,
    help="Choose from text files (general topics) or specific procrastination scripts"
)

# Always show update category button
if st.sidebar.button("Update Category", type="primary"):
    # Reset the study buddy when category is updated
    st.session_state.study_buddy = None
    st.session_state.current_category = None
    st.session_state.selected_category = category
    st.rerun()

# Show current active category under the button
if st.session_state.selected_category:
    st.sidebar.success(f"Category Updated to {st.session_state.selected_category}")

# Use the current category (either updated or previously selected)
current_category = st.session_state.selected_category if st.session_state.selected_category else category


# Input box for user query
user_input = st.chat_input("Please enter your query here!")

if user_input:
    # Update session state with the current user query
    st.session_state.current_user_query = user_input

    # Add user input to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Update chat history display immediately after user input
    display_chat_history()

    # Render a spinner while generating the response
    with st.spinner("Processing..."):
        # Generate response using the new ask_question function
        assistant_response = get_ai_response(category=current_category, query=user_input)

        # Update session state with the assistant's response
        st.session_state.current_response = assistant_response

        # Append the assistant's response to the chat history
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Update chat history display after receiving the assistant's response
    display_chat_history()

    print("*********************** start **************************")
    print("User input:", user_input)
    print("Category:", current_category)
    print("Assistant response:", st.session_state.current_response)
    print("*********************** END **************************", "\n\n")
