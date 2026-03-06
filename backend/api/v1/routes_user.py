from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database.db import get_db
from backend.repositories import review_repo
from backend.core.security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

#reviews api route
@router.get("/reviews")
def get_my_reviews(
        db: Session = Depends(get_db),
        current_user = Depends(get_current_user)):
    #fetches reviews from repository
    reviews = review_repo.get_reviews_by_user(db, current_user.id)

    return {
        "user": current_user.email,
        "reviews": reviews
    }