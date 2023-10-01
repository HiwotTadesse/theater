from models.user import User
from repositories.user_repository import UserRepository


class UserController:
     
    def __init__(self):
        self.userRepository = UserRepository()
    
    def createUser(self, user:User):
       return self.userRepository.createUser(user=user)
