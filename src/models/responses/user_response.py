from pydantic import BaseModel, Field

class UserResponse(BaseModel):
   userId : str
   status : str
    