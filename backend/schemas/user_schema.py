from pydantic import BaseModel, EmailStr
from pydantic import BaseModel, EmailStr, Field

#new user registers schema
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=72)

#user login schema
class UserLogin(BaseModel):
    email: str
    password: str

#token schema
class Token(BaseModel):
    access_token: str
    token_type: str