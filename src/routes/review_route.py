from fastapi import APIRouter, Query
from controller.review_controller import ReviewRateController

from controller.user_controller import UserController
from models.review import ReviewAndRating



class ReviewRateRouter:
    def __init__(self):
        self.router = APIRouter()
        self.reviewRateController = ReviewRateController()
    
    def setup_routes(self):
        @self.router.post("/reviews/",)
        def createReview(reviewAndRate:ReviewAndRating):
            return  self.reviewRateController.createReview(reviewAndRate=reviewAndRate)

        @self.router.get("/reviews/{userId}")
        def getReview(userId:str, page: int = Query(1, ge=1), per_page: int = Query(2, ge=1,)):
            return self.reviewRateController.getReview(userId=userId, per_page=per_page, page=page)
        
        
    def get_router(self):
        return self.router