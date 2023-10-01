import uuid
from bson import ObjectId
from fastapi import Form
from pydantic import BaseModel, Field

from typing import Annotated, Union

class Movie(BaseModel):
    imdbID: str  = Field(
        default=None, 
    )
    Title: str  = Field(
        default='', 
    )
    Year: str = Field(
        default='', 
    )
    Runtime: str = Field(
        default='', 
        exclude=True,
    )
    Genre: str = Field(
        default='',
        exclude=True,
    )
    Director: str = Field(
        default='', 
        exclude=True,
    )
    Writer: str = Field(
        default='',
        exclude=True,
    )
    Actors: str = Field(
        default='', 
        exclude=True,
    )
    Poster: str = Field(
        default='', 
    )
    Plot: Union[str, None] = Field(
        default='', 
        exclude=True,
    )
    Language: str = Field(
        default='', 
        exclude=True,
    )
    Type: str = Field(
        default='', 
    )


    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


    

    