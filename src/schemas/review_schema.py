def review_rate_serializer(reviewRate) -> dict:
        return {
            "reviewId":str(reviewRate["_id"]),
            "movieId":reviewRate["movieId"],
            "userId":reviewRate["userId"],
            "rating":reviewRate["rating"],
            "comment":reviewRate["comment"]
        }

def review_rates_serializer(reviewRates) -> list:
    return [review_rate_serializer(reviewRate) for reviewRate in reviewRates]
