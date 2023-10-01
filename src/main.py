
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routes.movie_route import MovieRouter
from routes.review_route import ReviewRateRouter
from routes.user_route import UserRouter


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def start():
    return {"Hello": "World"}

movie_router = MovieRouter()
movie_router.setup_routes()

user_router = UserRouter()
user_router.setup_routes()

review_router = ReviewRateRouter()
review_router.setup_routes()

app.include_router(movie_router.get_router())
app.include_router(user_router.get_router())
app.include_router(review_router.get_router())


        