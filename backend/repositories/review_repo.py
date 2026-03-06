from sqlalchemy.orm import Session
from backend.models.review_model import Review

# create review function
def create_review(db: Session, review_data: dict):
    #create review object
    review = Review(**review_data)
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

#to get review created by specific user
def get_reviews_by_user(db: Session, user_id: int):
    return db.query(Review).filter(Review.user_id == user_id).all()