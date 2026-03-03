from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creates SQLite DB
DATABASE_URL = "sqlite:///./ai_code_review.db"

#creating engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

#creating Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#defining base model class
Base = declarative_base()