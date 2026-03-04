from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#defining location and type of db
DATABASE_URL = "sqlite:///./code_review.db"

#creating db engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

#creating session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

#creating base class
Base = declarative_base()

print("DB FILE LOADED")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()