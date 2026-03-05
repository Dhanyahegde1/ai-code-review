from fastapi import FastAPI
from backend.core.config import get_settings
from pydantic import BaseModel
# Import the review API router created in routes_review.py
from backend.api.v1.routes_review import router as review_router


# Load application settings 
settings = get_settings()


# Initialize the FastAPI application
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


app.include_router(review_router)

#api Used to verify that the backend server is running properly

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }

# When someone visits port 8000 they will see this message

@app.get("/")
async def root():
    return {"message": "AI Code Review Backend is running"}

# API to connect all routes defined in routes_review.py

app.include_router(
    review_router,
    prefix="/api/v1",     
    tags=["Code Review"]   
)