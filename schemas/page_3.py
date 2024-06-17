from pydantic import BaseModel
from datetime import date
class User3Create(BaseModel):
    mobile_number: str
    first_name: str
    last_name: str
    dob: date

class User3Response(BaseModel):
    id : int
    mobile_number: str
    first_name: str
    last_name: str
    dob: date

    class Config:
        orm_mode = True
