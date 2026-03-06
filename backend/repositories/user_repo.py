from sqlalchemy.orm import Session
from backend.models.user_model import User

#to get user from db using email
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

#creates new user in db
def create_user(db: Session, user_data):
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user