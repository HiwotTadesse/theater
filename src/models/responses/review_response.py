from pydantic import BaseModel, Field

class ReviewResponse(BaseModel):
   reviewId : str
   status : str
    