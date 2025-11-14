# Streamlit run command :
    uv run streamlit run streamlit_app.py


# DragonFly postman API :
    This is the API for DragonFly, an AI-powered study assistance tool that helps students improve their study habits and overcome procrastination.
    ####### execution steps :
        1. Execute in postman:
        2. GET http://localhost:8000/get_all_categories
        3. POST http://localhost:8000/ask_question
        with body :
        {
            "category": "TimeManagement",
            "query": "How do I prioritize my tasks?"
        }
        4. Response will be like :
        {
            "category": "TimeManagement",
            "query": "How do I prioritize my tasks?",
            "response": "AI generated response based on the TimeManagement content..."
        }


# build docker :
1. docker build -t dragonfly-api . 
2. docker run -d -p 8000:8000 --name dragonfly-container --env-file .env dragonfly-api
3. docker ps --> View container status
4. docker stop dragonfly-container --> To stop container
5. docker rm dragonfly-container --> To remove container
6. docker rmi dragonfly-api --> To remove image

docker run -d -p 8501:8501 --name dragonfly-streamlit-container -e OPENAI_API_KEY="$(grep OPENAI_API_KEY .env | cut -d '=' -f2 | tr -d '\"')" -e LANGCHAIN_API_KEY="$(grep LANGCHAIN_API_KEY .env | cut -d '=' -f2 | tr -d '\"')" -e LANGCHAIN_TRACING_V2="true" -e LANGCHAIN_PROJECT="dragonfly" dragonfly-streamlit