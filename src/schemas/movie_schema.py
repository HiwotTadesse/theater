def movie_serializer(movie) -> dict:
        return {
            'movieId':str(movie["_id"]),
            'Title':movie["Title"],
            'Year':movie["Year"],
            'Poster':movie["Poster"],
            'Type':movie["Type"],
            'status': "Success" if str(movie["_id"]) is not None else "Error"
        }

def movies_serializer(movies) -> list:
    return [movie_serializer(movie) for movie in movies]
