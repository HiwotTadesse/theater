from typing import Annotated
from fastapi import Depends, Form, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.params import Query
from pydantic import parse_obj_as
from helpers.objectId_helper import validate_id
from helpers.pagination_helper import paginationHelper
from models.helpers.search_movie_helper import SearchMovieHelper
from models.movie import Movie
from models.status import Status
from omdbApiServices.omdb_movie_api_service import OMDBMovieApiService
from repositories.movie_repository import MovieRepository

from schemas.movie_schema import movie_serializer


class MovieController:

    def __init__(self):
        self.movieRepository = MovieRepository()
        self.OMDBMovieApiService = OMDBMovieApiService()

    def createMovie(self, Title: Annotated[str, Form()],
        Year: Annotated[str, Form()],
        Runtime: Annotated[str, Form()],
        Genre: Annotated[str, Form()],
        Director: Annotated[str, Form()],
        Writer: Annotated[str, Form()],
        Actors: Annotated[str, Form()],
        Poster: UploadFile,
        Plot: Annotated[str, Form()],
        Language: Annotated[str, Form()],
        Type: Annotated[str, Form()] ):
        return  self.movieRepository.createMovie(Title=Title,Year=Year, Runtime=Runtime, Genre=Genre,Director=Director, Writer=Writer,Actors=Actors, Poster=Poster, Plot=Plot, Language=Language, Type=Type)

    def getMovie(self, id: str):
        return self.OMDBMovieApiService.getMovie(id=id)
        
    def searchMovie(self,title:str, year: str, page: int = Query(1, ge=1), per_page: int = Query(2, ge=1,)):
        return self.OMDBMovieApiService.searchMovie(title=title, year=year, page=page, per_page=per_page)
    