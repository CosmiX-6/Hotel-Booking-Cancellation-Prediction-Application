from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class ProcessSchema(BaseModel):
    name : str = Field(...)
    age : int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name" : "Jeff Bezos",
                "age" : 25
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}