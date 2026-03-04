from fastapi import FastAPI
from backend.database.db import engine , Base
from backend.models import user_model, review_model
from fastapi.middleware.cors import CORSMiddleware

#creating db tables
Base.metadata.create_all(bind=engine)

#creating FastApi app
app = FastAPI()

#cors config
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#authentication API routes
from backend.api.v1.routes_auth import router as auth_router
#attaches all auth routes to the FastAPI application
app.include_router(auth_router)

#user route
from backend.api.v1.routes_user import router as user_router
#user route api active
app.include_router(user_router)

@app.get("/")
def health_check():
    return {"status": "Server running"}