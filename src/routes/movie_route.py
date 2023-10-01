from typing import Annotated
from fastapi import APIRouter, Depends, Form, Query, UploadFile
from pymongo import MongoClient

from controller.movie_controller import MovieController

class MovieRouter:
    def __init__(self):
        self.router = APIRouter()
        self.movieController = MovieController()
    
    
    def setup_routes(self):
        @self.router.post("/movies/")
        async def createMovie(Title: Annotated[str, Form()],
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
            return self.movieController.createMovie(Title=Title,Year=Year, Runtime=Runtime, Genre=Genre,Director=Director, Writer=Writer,Actors=Actors, Poster=Poster, Plot=Plot, Language=Language, Type=Type,)
        
        @self.router.get("/movies/{id}")
        async def getMovieById(id):
            return self.movieController.getMovie(id)
        
        @self.router.get("/movies/")
        async def searchMoviesByTitleAndYear(title:str, year: str, page: int = Query(1, ge=1), per_page: int = Query(2, ge=1,)):
            return self.movieController.searchMovie(title, year, page, per_page)
        

    def get_router(self):
        return self.router