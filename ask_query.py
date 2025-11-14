from main import StudyBuddy


# Function for API usage
def ask_question(category, query, base_directory="cleaned_data"):
    """Function for API to get responses"""
    try:
        # Initialize StudyBuddy 
        study_buddy = StudyBuddy(base_directory=base_directory)
        
        # Load knowledge base 
        if not study_buddy.load_knowledge_base_for_category(category):
            return f"Failed to load knowledge base for category: {category}"
        
        # Prepare agent 
        study_buddy.prepare_prompt_create_agent()
        
        # Get response
        response = study_buddy.ask_query(category, query)
        return response
        
    except Exception as e:
        return f"Error processing question: {e}"


# main function for testing
def main():
    """Simple main function for interactive session"""
    category = "Conquering Rebellion Procrastination (22-Minute Call)"
    query = "What's the specific task or expectation that you find yourself resisting the most right now?"
        
    response = ask_question(category, query)
    print("\n\n&"*15)
    print(f"\nQuery: {query}")
    print(f"AI Response: {response}")
    print("#"*15)    


##################################################################################################
if __name__ == "__main__":
    main()
    