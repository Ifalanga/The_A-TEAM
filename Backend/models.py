import pydantic
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    username: str
    email: str
    full_name: str
    password: str
    interest: str
    level: str


class Course(BaseModel):
    namecourse: str
    username: str



