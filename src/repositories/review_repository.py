import logging
import pprint
from bson import ObjectId
from fastapi import HTTPException, Query, status
from fastapi.responses import JSONResponse
from pymongo import MongoClient
from config.settings import Settings
from helpers.objectId_helper import validate_id
from models.helpers.review_search_helper import ReviewHelper
from models.responses.review_response import ReviewResponse
from models.review import ReviewAndRating
from models.status import Status
from schemas.review_schema import review_rates_serializer
from schemas.user_schema import user_serializer, users_serializer
logging.basicConfig(level=logging.INFO)  # Set the desired logging level

logger = logging.getLogger(__name__) 

class ReviewAndRateRepository:

    def __init__(self):
        self.appSettings  = Settings()
        self.client = MongoClient(self.appSettings.mongoClient)
        self.db = self.client['theater']
        self.collection = self.db["review_and_rate"]

    def create_collection_if_not_exists(self, collection_name: str):

        if collection_name not in self.db.list_collection_names():
            self.db.create_collection(collection_name)

    def createReview(self, reviewAndRate:ReviewAndRating):
        self.create_collection_if_not_exists(collection_name="review_and_rate")
        userCollection = self.db["user"]
        
        if(validate_id(reviewAndRate.userId)):
            existing_user =  users_serializer(userCollection.find({"_id": ObjectId(reviewAndRate.userId)}))
        
            if len(existing_user) > 0 :
                review = self.collection.insert_one(dict(reviewAndRate))
                return ReviewResponse(reviewId= str(review.inserted_id), status= "Success")
            else:
              return Status(
                    status_code=404,
                    statusMessage= "User not found",
                    status="Error"
                )
        else:
            error = ValueError("Invalid object ID")
            return Status(
                    status_code=400,
                    statusMessage=str(error),
                    status="Error"
                )

        
    def getReview(self, userId: str, page: int = Query(1, ge=1), per_page: int = Query(2, ge=1,)):
        skip_count = (page - 1) * per_page
        reviews = review_rates_serializer(self.collection.find({"userId": userId}).skip(skip_count).limit(per_page))

        reviews = ReviewHelper(
            data=reviews,
            status = "Success",
            page = page,
            per_page = per_page,
            totalResults = self.collection.count_documents({"userId": userId}))

        return reviews
    
