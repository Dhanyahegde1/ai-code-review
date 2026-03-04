from pydantic import BaseModel


class CodeReviewRequest(BaseModel):
    code: str


class CodeReviewResponse(BaseModel):
    message: str
    status: str