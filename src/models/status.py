from pydantic import BaseModel, Field

class Status(BaseModel):
    statusMessage: str
    status: str
    status_code: int = Field(default=None)
    