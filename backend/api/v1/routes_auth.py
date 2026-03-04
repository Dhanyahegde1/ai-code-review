from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.dependencies import get_db
from backend.schemas.user_schema import UserCreate, UserLogin, Token
from backend.repositories import user_repo
from backend.core.security import hash_password, verify_password, create_access_token

#creating router
router = APIRouter(prefix="/auth", tags=["Auth"])

#register api route
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:   
        #checks if email is exists
        existing_user = user_repo.get_user_by_email(db, user.email)
        if existing_user:
            raise HTTPException(status_code=400, detail="email already exists")
        #hash password
        hashed_pw = hash_password(user.password)
        #create user
        new_user = user_repo.create_user(
            db,
            {
                "username": user.username,
                "email": user.email,
                "hashed_password": hashed_pw
            }
        )
        return {"message": "User created successfully"}
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unexpected error occurred"
        )

#login api route
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        #fetch user
        db_user = user_repo.get_user_by_email(db, user.email)
        #validate credentials
        if not db_user or not verify_password(user.password, db_user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        #generate JWT token
        token = create_access_token({"sub": db_user.email})

        return {"access_token": token, "token_type": "bearer"}
    
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unexpected error occurred"
        )