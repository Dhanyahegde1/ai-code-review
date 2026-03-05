from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

#connecting security layer to db layer
from backend.database.db import get_db
from backend.repositories import user_repo

#jwt config
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

#password hashing
pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    deprecated="auto"
)
#Oauth2 token tracker
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

#reads token , decodes, finds user in db
def get_current_user(token: str = Depends(oauth2_scheme),
                     db: Session = Depends(get_db)):

    try:
        #decode JWT 
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #extract email
        email = payload.get("sub")
        #validate token
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    #get user from datbase
    user = user_repo.get_user_by_email(db, email)

    if user is None:
        raise HTTPException(status_code=401, detail="User not found")

    return user

#password hashing function
def hash_password(password: str):
    return pwd_context.hash(password)

#password verification
def verify_password(plain_password:str, hashed_password:str):
    return pwd_context.verify(plain_password, hashed_password)

#jwt token creation
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)