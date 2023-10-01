from bson import ObjectId
from pydantic import BaseModel, Field

class ReviewAndRating(BaseModel):
    movieId: str = Field(alias='movieId')
    userId: str = Field(alias='userId')
    rating: float = Field(ge=1, le=10)
    comment: str = Field(
        default=None, 
    )
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}