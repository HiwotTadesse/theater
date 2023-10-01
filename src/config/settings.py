from fastapi import FastAPI
from pydantic import Field
from pydantic_settings import BaseSettings
from pymongo import MongoClient


class Settings(BaseSettings):
    app_name: str = Field("Theater")
    OMDBAPIURL: str = Field(default="http://www.omdbapi.com/?apikey=6bd1dfad")
    mongoClient: str = Field(default="mongodb://localhost:27017")