from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field, constr, validator

class User(BaseModel):
    username: constr(min_length=6, max_length=30, pattern=r"^[a-zA-Z][a-zA-Z0-9_]+$",)
    email: EmailStr
    
    class Config:
        from_attributes = True
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}