from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ask_query import ask_question
from typing import List

app = FastAPI(title="DragonFly AI API", description="AI-powered study assistance API", version="1.0.0")

# Request model for get_response endpoint
class QueryRequest(BaseModel):
    category: str
    query: str

# Response model
class QueryResponse(BaseModel):
    category: str
    query: str
    response: str

# Hardcoded categories
CATEGORIES = [
    # Text file categories
    "StudySkills",
    "ProcrastinationHack", 
    "TimeManagement",
    "CrunchTime",
    "Introduction",
    
    # DOCX file categories
    "Conquering Fear-Based Procrastination (22-Minute Call)",
    "Conquering Rebellion Procrastination (22-Minute Call)",
    "Conquering Deadline Procrastination (22-Minute Call)",
    "Conquering Decision Procrastination (22-Minute Call)",
    "Conquering Task Overwhelm Procrastination (22-Minute Call)",
    "Conquering Lack of Interest Procrastination (22-Minute Call)",
    "Conquering Perfectionism Procrastination (22-Minute Call)",
    "Conquering Decision Paralysis (22-Minute Call)",
    "Conquering Perfectionist Procrastination (22-Minute Call)",
    "Conquering Avoidant Procrastination (22-Minute Call)",
    "Conquering Decision Paralysis Procrastination (22-Minute Call)",
    "Conquering Deadline Adrenaline Procrastination (22-Minute Call)",
    "Conquering Distraction Procrastination (22-Minute Call)",
    "Conquering Productive Procrastination (22-Minute Call)",
    "Conquering Fear of Failure Procrastination (22-Minute Call)",
    "Conquering Energy Depletion Procrastination (22-Minute Call)",
    "Conquering Unclear Goals Procrastination (22-Minute Call)",
    "Conquering Skill Gap Procrastination (22-Minute Call)",
    "Conquering Pleasure-Seeking Procrastination (22-Minute Call)",
    "Conquering Arousal Procrastination (22-Minute Call)",
    "Conquering Bedtime Procrastination (22-Minute Call)"
]

@app.get("/get_all_categories", response_model=List[str])
async def get_all_categories():
    """Get all available study categories"""
    return CATEGORIES

@app.post("/get_response", response_model=QueryResponse)
async def get_response(request: QueryRequest):
    """Get AI response for a query in a specific category"""
    try:
        # Validate category
        if request.category not in CATEGORIES:
            raise HTTPException(
                status_code=400, 
                detail=f"Invalid category. Available categories: {CATEGORIES}"
            )
        
        # Get response using the ask_question function
        response = ask_question(request.category, request.query)
        
        return QueryResponse(
            category=request.category,
            query=request.query,
            response=response
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)