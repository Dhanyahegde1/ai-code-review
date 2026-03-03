from fastapi import FastAPI

app = FastAPI(
    title="AI Code Review Backend",
    version="1.0.0"
)

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "python_version": "3.11.9",
        "module": "review-module"
    }

@app.get("/")
async def root():
    return {"message": "AI Code Review Backend Running"}