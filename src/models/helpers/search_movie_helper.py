from typing import List
from pydantic import BaseModel

from models.movie import Movie

class SearchMovieHelper(BaseModel):
    data: List[Movie]
    totalResults: int
    page: int
    per_page: int
    status: str