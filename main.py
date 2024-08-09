from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx
from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Text-to-Speech API",
    description="A FastAPI service that converts text to speech using a local LLM.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

LLM_SERVICE_URL = os.getenv("LLM_SERVICE_URL")

class TextToSpeechRequest(BaseModel):
    text: str

@app.get("/api/health", summary="Health check endpoint")
async def health_check():
    """
    Perform a health check on the API.
    """
    return {"message": "I am healthy"}

@app.post("/api/text-to-speech", summary="Convert text to speech")
async def text_to_speech(request: TextToSpeechRequest):
    """
    Convert the given text to speech using the LLM service.
    """
    if not LLM_SERVICE_URL:
        return {"error": "LLM_SERVICE_URL is not set"}
    
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{LLM_SERVICE_URL}/convert", json={"text": request.text})
        if response.status_code == 200:
            return {"audio_data": response.content}
        else:
            return {"error": "Failed to convert text to speech"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)