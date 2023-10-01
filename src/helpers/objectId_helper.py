from bson import ObjectId
from fastapi.responses import JSONResponse


def validate_id(v: str)-> bool:
    if not ObjectId.is_valid(v):
        return False
    return True

