from fastapi import FastAPI
from rag import ask
from pydantic import BaseModel

# Define the FastAPI application
app = FastAPI(
    title="Industrial Document Intelligence Platform",
    version="1.0"
)

# Health check endpoint to verify that the API is running.
@app.get("/health")
def health():

    return {
        "status": "UP"
    }


# Define a Pydantic model for the request body when asking a question.
class QuestionRequest(BaseModel):
    question: str
    
# Define an endpoint to ask questions and get answers from the RAG system.
@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        answer = ask(request.question)

        return {
            "question": request.question,
            "answer": answer
        }
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
# Root endpoint
@app.get("/")
def root():

    return {
        "application":
        "Industrial Document Intelligence Platform"
    }