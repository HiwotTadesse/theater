from fastapi.encoders import jsonable_encoder
import requests
from pydantic import parse_obj_as
from fastapi.params import Query

from config.settings import Settings
from helpers.objectId_helper import validate_id
from helpers.pagination_helper import paginationHelper
from models.helpers.search_movie_helper import SearchMovieHelper
from models.movie import Movie
from models.status import Status
from repositories.movie_repository import MovieRepository


class OMDBMovieApiService:
    
    def __init__(self):
        self.appSettings  = Settings()
        self.omdbApiUrl = self.appSettings.OMDBAPIURL
        self.movieRepository = MovieRepository()
        
    def getMovie(self, id: str):

        if(validate_id(id)):
            movie = self.movieRepository.getMovieById(id)
            if len(movie) > 0 :
                return movie[0]
            else:
                self.getMovieFromApi(id)    
        else:
          return self.getMovieFromApi(id)    
        
        
    def getMovieFromApi(self, id: str):
        response = requests.get(f'{self.omdbApiUrl}&i={id}')

        if response.status_code == 200:
            movie = response.json()
            if movie['Response'] == "True":
                movie =  jsonable_encoder(parse_obj_as(Movie, movie))
                movie["status"]= "Success"
                return movie
            else:
                return Status (statusMessage="No movie id found.", status= "Success",status_code=response.status_code)
        else:
            return Status(statusMessage= "Failed to fetch data from the API", status="Error", status_code=response.status_code )
    

    def searchMovie(self,title:str, year: str,page: int = Query(1, ge=1), per_page: int = Query(2, ge=1,)):
        
        movieFromDb = self.movieRepository.searchMovieFromDB(title=title, year=year)
        
        response = requests.get(f'{self.omdbApiUrl}&s={title}&y={year}')
        
        if response.status_code == 200:
            data = response.json()
            if data["Response"] == "True" or len(movieFromDb) > 0:
                
                mergedData = movieFromDb + data["Search"]
                paginatedData = paginationHelper(data=mergedData, per_page=per_page, page=page)
                totalResults = int(data["totalResults"]) + len(movieFromDb)

                searchResult =  SearchMovieHelper(data = paginatedData ,status = "Success",page = page,per_page = per_page,totalResults = totalResults)
                return searchResult
            else:
               searchResult =  SearchMovieHelper(data = [],status = "Success",page = page,per_page = per_page,totalResults = 0)
               return searchResult
        else:
            return Status(statusMessage= "Failed to fetch data from the API", status="Error", status_code=response.status_code)
        