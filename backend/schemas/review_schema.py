# Import BaseModel from Pydantic
# Pydantic is used by FastAPI to validate request and response data
from pydantic import BaseModel


# Schema for the incoming request body
# This defines the structure of data that the client must send
class CodeReviewRequest(BaseModel):

    # The code snippet that needs to be reviewed
    # Example request:
    # {
    #     "code": "print('Hello World')"
    # }
    code: str


# Schema for the API response
# This ensures the response returned by the API follows a fixed structure
class CodeReviewResponse(BaseModel):

    # Status of the operation (success or error)
    status: str

    # Message describing the result of the operation
    message: str