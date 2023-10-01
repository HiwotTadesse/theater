import json
import shutil
from typing import Annotated
import uuid
from bson import ObjectId
from fastapi import Depends, Form, HTTPException, Query, UploadFile
from pymongo import MongoClient
from config.settings import Settings
from helpers.upload_image_helper import uploadImage
from models.movie import Movie
from models.responses.movie_response import MovieResponse

from schemas.movie_schema import movie_serializer, movies_serializer

class MovieRepository:

    def __init__(self):
        self.appSettings  = Settings()
        self.client = MongoClient(self.appSettings.mongoClient)
        self.db = self.client['theater']
        self.collection = self.db["movie"]


    def create_collection_if_not_exists(self, collection_name: str):

        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

    def getMovieById(self, movieId:str):
        movie = self.collection.find({"_id": ObjectId(movieId)})
        return movies_serializer(movie)
       

    def createMovie(self,Title: Annotated[str, Form()],
        Year: Annotated[str, Form()],
        Runtime: Annotated[str, Form()],
        Genre: Annotated[str, Form()],
        Director: Annotated[str, Form()],
        Writer: Annotated[str, Form()],
        Actors: Annotated[str, Form()],
        Poster: UploadFile,
        Plot: Annotated[str, Form()],
        Language: Annotated[str, Form()],
        Type: Annotated[str, Form()]):
        
        self.create_collection_if_not_exists(collection_name="movie")        
        uploadedImagePath = uploadImage(Poster)
        
        movie = Movie(
            Title=Title,Year=Year, Runtime=Runtime, Genre=Genre,Director=Director, Writer=Writer,Actors=Actors, Plot=Plot,Poster=uploadedImagePath, Language=Language, Type=Type
        )
        insertedMovie = self.collection.insert_one(dict(movie))
        return MovieResponse(movieId= str(insertedMovie.inserted_id), status ="Success")

    def searchMovieFromDB(self, title:str, year: str,):
        movies = movies_serializer(self.collection.find({"Title":title, "Year": year,}))
        return movies

    