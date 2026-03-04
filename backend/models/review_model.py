from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from backend.database.db import Base

#creating review model
class Review(Base):
    #table name
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    code_snippet = Column(Text, nullable=False)
    result = Column(Text)
    score = Column(Integer)

    #foreign key (this links the review to a user)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User")