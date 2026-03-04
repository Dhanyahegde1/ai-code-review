# Import Depends from FastAPI
# Depends is used for dependency injection in FastAPI routes
from fastapi import Depends

# Import Session class from SQLAlchemy
# Session is used to interact with the database (queries, inserts, updates)
from sqlalchemy.orm import Session

# Import SessionLocal which creates database session instances
# This is defined in: backend/database/db.py
from database.db import SessionLocal


# Dependency function to provide a database session
# This function will be used in API routes whenever database access is needed
def get_db():

    # Create a new database session
    db = SessionLocal()

    try:
        # Yield the database session to the API route
        # FastAPI temporarily provides this session to the route handler
        yield db

    finally:
        # After the request is completed, close the session
        # This prevents memory leaks and unused database connections
        db.close()