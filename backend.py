from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from ai_agent import fetch_response_from_ai

class RequestState(BaseModel):
    llm_id:str
    user_query:List[str]
    allow_search:bool

app = FastAPI()

ALLOWED_MODELS = ["qwen-qwq-32b", "llama-3.3-70b-versatile"];

@app.post('/chat')
def get_response(request: RequestState):
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    # return error if not in allowed models;
    if (request.llm_id not in ALLOWED_MODELS):
        return {"error": "Invalid model name. Kindly select a valid AI model"}

    # Create AI Agent and get response from it! 
    response= fetch_response_from_ai(request.user_query, request.allow_search, request.llm_id)
    return response

if __name__ == "__main__":
    # use unicorn to run 
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=9999)