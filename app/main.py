from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title="AI Code Review API",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/test")
def test_post(data: dict):
    return {"received": data}

@app.get("/")
def root():
    return {"message": "AI Code Review API is running"}
