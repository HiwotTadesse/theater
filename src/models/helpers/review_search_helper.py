from typing import List
from pydantic import BaseModel

from models.review import ReviewAndRating

class ReviewHelper(BaseModel):
    data: List[ReviewAndRating]
    totalResults: int
    page: int
    per_page: int
    status: str