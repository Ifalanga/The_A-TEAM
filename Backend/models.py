from pydantic import BaseModel


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



