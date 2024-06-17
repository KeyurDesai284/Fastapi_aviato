from pydantic import BaseModel

class User1Create(BaseModel):
    company_name: str
    first_name: str
    last_name: str
    email: str
    password: str

class User1Response(BaseModel):
    id: int
    company_name: str
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True