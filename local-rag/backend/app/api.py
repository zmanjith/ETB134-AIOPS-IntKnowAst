from fastapi import FastAPI, HTTPException
from rag.rag_service import RagService
from pydantic import BaseModel


# Define the FastAPI application
app = FastAPI(
    title="Industrial Document Intelligence Platform",
    version="1.0"
)

rag_service = RagService()

# Health check endpoint to verify that the API is running.
@app.get("/health")
def health():

    return {
        "status": "Up and running"
    }


# Define a Pydantic model for the request body when asking a question. Pydantic model is concept of creating a customised class object
# a customised class object is returning as a JSON object to the user. The user can send a question in the request body, and it will be validated against this model.
# model format will be defined under thast class. Here its accepting a parater : question.
class QuestionRequest(BaseModel):
    question: str
   
# Define an endpoint to ask questions and get answers from the RAG system.
# here its POST request. So we are expecting a value return, for the input we have given.
# Input is a pydantic class object. Then returing a answer.
# exceptio is captured since POST will have 404 errors like items not found.
@app.post("/ask")
def ask_question(request: QuestionRequest):
    try:
        return rag_service.ask(request.question)
    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        
# Root endpoint
@app.get("/")
def root():

    return {
        "Application":
        "Industrial Document Intelligence Platform"
    }