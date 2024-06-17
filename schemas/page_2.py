from pydantic import BaseModel


class User2Create(BaseModel):
    mobile_number : str
    first_name : str
    last_name : str
    hashtag : str

class User2Response(BaseModel):
    id : int
    mobile_number : str
    first_name : str
    last_name : str
    hashtag : str

    class Config:
        orm_mode = True