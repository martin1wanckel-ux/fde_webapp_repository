from fastapi import FastAPI
from src.config.config import Config
from dataclasses import asdict
import json
# start simple 
app = FastAPI()

@app.get("/")

async def root():
    return{"message" : "Hello World"}

@app.get("/health")

async def health():
    return {"status": "ok"}

@app.get("/config")

async def config():
    config = Config.from_env()
    return asdict(config)

#common checklist 

# python -m venv .venv
# .\.venv\Scripts\Activate.ps1
# pip install "fastapi[standard]"
# uvicorn src.api.main:app --reload