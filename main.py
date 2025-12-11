from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from core.brain import AletheiaBrain
import time
from dotenv import load_dotenv
import os

# 加载环境变量
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

brain = AletheiaBrain(mode="compatible")


class Query(BaseModel):
    text: str


@app.get("/")
async def root():
    return {"message": "Zen-Ask Backend is running", "version": "1.0.0"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.post("/api/ask")
async def ask(query: Query):
    answer = brain.think(query.text)
    return {"answer": answer}


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
