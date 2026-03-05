# Import FastAPI framework to build the backend API
from fastapi import FastAPIs
from core.config import get_settings
from pydantic import BaseModel

# Import the review API router created in routes_review.py
from api.v1.routes_review import router as review_router


# Load application settings (app name, version, DB config, etc.)
settings = get_settings()


# Initialize the FastAPI application
# The title and version appear in Swagger documentation
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)


app.include_router(review_router)


# Health check endpoint
# Used to verify that the backend server is running properly
# Useful for monitoring tools, load balancers, and debugging

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version
    }


# Root endpoint of the API
# When someone visits http://127.0.0.1:8000/
# they will see this message
@app.get("/")
async def root():
    return {"message": "AI Code Review Backend is running"}


# Register Review API Router
# This connects all routes defined in routes_review.py
# to the main FastAPI application
app.include_router(
    review_router,
    prefix="/api/v1",      # All routes will start with /api/v1
    tags=["Code Review"]   # Used for grouping endpoints in Swagger UI
)