from pymongo import MongoClient
from config.settings import Settings
from models.responses.user_response import UserResponse
from models.status import Status
from models.user import User
from schemas.user_schema import user_serializer


class UserRepository:

    def __init__(self):
        self.appSettings  = Settings()
        self.client = MongoClient(self.appSettings.mongoClient)
        self.db = self.client['theater']
        self.collection = self.db["user"]

    def create_collection_if_not_exists(self, collection_name: str):

        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

    def createUser(self, user:User):
        
        self.create_collection_if_not_exists(collection_name="user")
        if self.is_username_unique(user.username):
            insertedUser =  self.collection.insert_one(dict(user))
            return UserResponse(userId= str(insertedUser.inserted_id), status= "Success")
        else:
            return Status(statusMessage="Username already exists.", status= "Error")

    def is_username_unique(self, username: str) -> bool:
        existing_user = self.collection.find_one({"username": username})
        if existing_user:
            return False  
        else:
            return True 