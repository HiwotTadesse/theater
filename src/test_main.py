from fastapi.testclient import TestClient
from helpers.upload_image_helper import uploadImage
from main import app

client = TestClient(app)   

def test_read_movie_with_id_not_found():
    response = client.get("movies/12353345",)
    assert response.status_code == 200
    assert response.json() == {
        "statusMessage": "No movie id found.",
        "status": "Success",
        "status_code": 200
        }
    
def test_read_movie_by_movieId():
    response = client.get("movies/65182c36f4d8dd739aab29c2",)
    assert response.status_code == 200
    assert response.json() == {
                "movieId": "65182c36f4d8dd739aab29c2",
                "Title": "dgjdgfh",
                "Year": "ksjjgsd",
                "Poster": "static/images/871605ad-5c8d-449e-b56a-1f976c5dee67.jpg",
                "Type": "movie",
                "status": "Success"
                }
    
def test_read_movie_by_imdbID():
    response = client.get("movies/tt3896198",)
    assert response.status_code == 200
    assert response.json() == {
                "imdbID": "tt3896198",
                "Title": "Guardians of the Galaxy Vol. 2",
                "Year": "2017",
                "Poster": "https://m.media-amazon.com/images/M/MV5BNjM0NTc0NzItM2FlYS00YzEwLWE0YmUtNTA2ZWIzODc2OTgxXkEyXkFqcGdeQXVyNTgwNzIyNzg@._V1_SX300.jpg",
                "Type": "movie",
                "status": "Success"
                }
    
def test_write_movie():
    filename = "static/images/08d768e9-2f67-4768-98e5-6009c88ec28c.jpg"
        
    form_data = {
        "Title": "Hobbit",
        "Year": "1977",
        "Runtime": "90 min",
        "Genre": "Animation, Adventure, Family",
        "Director": "Jules Bass, Arthur Rankin Jr.",
        "Writer": "J.R.R. Tolkien, Romeo Muller",
        "Actors": "Orson Bean, John Huston, Theodore Gottlieb",
        "Plot": "A homebody hobbit in Middle Earth gets talked into joining a quest with a group of dwarves to recover their treasure from a dragon.",
        "Language": "English",
        "Type": "movie"
    }
    
    response = client.post("movies/",data=form_data, files={"Poster": ("filename", open(filename, "rb"), "image/jpeg")})
    assert response.status_code == 200
    assert response.json()["status"] == "Success" 
                
def test_search_movie():
                response = client.get("/movies/?title=hobbit&year=2014&page=1&per_page=2")
                assert response.status_code == 200
                assert response.json() == {
                    "data": [
                        {
                        "imdbID": "",
                        "Title": "hobbit",
                        "Year": "2014",
                        "Poster": "static/images/3134d83c-6a5e-4dc7-bdb6-d56ffe1baa9d.jpg",
                        "Type": "movie"
                        },
                        {
                        "imdbID": "tt2310332",
                        "Title": "The Hobbit: The Battle of the Five Armies",
                        "Year": "2014",
                        "Poster": "https://m.media-amazon.com/images/M/MV5BMTYzNDE3OTQ3MF5BMl5BanBnXkFtZTgwODczMTg4MjE@._V1_SX300.jpg",
                        "Type": "movie"
                        }
                    ],
                    "totalResults": 16,
                    "page": 1,
                    "per_page": 2,
                    "status": "Success"
                    }


def test_write_users():
    response = client.post("users/", json={
        "username": "hiwottadesse",
        "email": "user@example.com"
        })
    assert response.status_code == 200
    assert response.json()["status"] == "Success"
    
def test_write_users_repeated_username():
    response = client.post("users/", json={
    "username": "hiwottadesse",
    "email": "user@example.com"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "Error"
    assert response.json()["statusMessage"] == "Username already exists."
    
def test_write_reviews():
    response = client.post("reviews/", json={
        "movieId": "8933489394",
        "userId": "65183c0243896674d7590af4",
        "rating":  6.5,
        "comment": "Whiplash (2014), directed and written by Damien Chazelle, is a film mainly about the relationship between a music teacher and his student, "
        })
    assert response.status_code == 200
    assert response.json()["status"] == "Success"

def test_read_reviews():
    response = client.get("reviews/65183c0243896674d7590af4")
    assert response.status_code == 200
    assert response.json() == {
        "data": [
            {
            "movieId": "8933489394",
            "userId": "65183c0243896674d7590af4",
            "rating": 6.5,
            "comment": "Whiplash (2014), directed and written by Damien Chazelle, is a film mainly about the relationship between a music teacher and his student, "
            }
        ],
        "totalResults": 1,
        "page": 1,
        "per_page": 2,
        "status": "Success"
        }

def test_write_reviews_with_invalid_objectId():
    response = client.post("reviews/", json={
  "movieId": "8933489394",
  "userId": "2732534752",
  "rating":  6.5,
  "comment": "Whiplash (2014), directed and written by Damien Chazelle, is a film mainly about the relationship between a music teacher and his student, "
})
    assert response.status_code == 200
    assert response.json() == {
            "statusMessage": "Invalid object ID",
            "status": "Error",
            "status_code": 400
            }
    
def test_write_reviews_with_id_not_found():
    response = client.post("reviews/", json={
    "movieId": "8933489394",
    "userId": "6512ac8213d50f935cccff11",
    "rating":  6.5,
    "comment": "Whiplash (2014), directed and written by Damien Chazelle, is a film mainly about the relationship between a music teacher and his student, "
    })
    assert response.status_code == 200
    assert response.json() == {
        "statusMessage": "User not found",
        "status": "Error",
        "status_code": 404
        } 
    

 