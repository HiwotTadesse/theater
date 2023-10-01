from pydantic import BaseModel, Field

class MovieResponse(BaseModel):
   movieId : str
   status : str
    