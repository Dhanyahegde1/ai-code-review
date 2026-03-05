from fastapi import Depends
from sqlalchemy.orm import Session
from database.db import SessionLocal


# function to provide db access
def get_db():

    # Create a new database session
    db = SessionLocal()

    try:
        
        # FastAPI temporarily provides this session to the route handler
        yield db

    finally:
        db.close()