from fastapi import APIRouter

from controller.user_controller import UserController
from models.user import User


class UserRouter:
    def __init__(self):
        self.router = APIRouter()
        self.userController = UserController()
    
    def setup_routes(self):
        @self.router.post("/users/")
        async def createUser(user: User):
            return self.userController.createUser(user=user)
        
    def get_router(self):
        return self.router