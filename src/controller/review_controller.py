from fastapi import Query
from models.review import ReviewAndRating

from repositories.review_repository import ReviewAndRateRepository


class ReviewRateController:
     
    def __init__(self):
        self.reviewAndRateRepository = ReviewAndRateRepository()
    
    def createReview(self, reviewAndRate:ReviewAndRating):
       return self.reviewAndRateRepository.createReview(reviewAndRate=reviewAndRate)

    def getReview(self, userId:str, page: int = Query(1, ge=1), per_page: int = Query(2, ge=1,)):
       return  self.reviewAndRateRepository.getReview(userId=userId, page=page, per_page=per_page)
