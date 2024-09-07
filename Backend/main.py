from fastapi import FastAPI, Depends, HTTPException
import database as db
from models import User,Course
import bcrypt

app = FastAPI()
# Generate a strong salt
salt = bcrypt.gensalt()

@app.post("/user")
def add_user(user: User):
    if db.get_user(user.username) is not None:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password with salt
    print(user.password)
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), salt)

    user.password = hashed_password
    print(user.password)
    db.insert_user(user)

@app.get("/user/{user_name}")
def get_user() -> User:
    return "user details"

@app.put("/username")
def update_user(user: User):
    return "user"


@app.get("/courses")
def get_courses(course: str, level: str):
    return {"course": course, "level": level}


@app.get("/similarcourses")
def get_similar_courses(course: str):
    return "similar"

@app.get("/courses/{userid}")
def get_completed_courses(username: str):
    courses = db.get_user_courses(username)
    return courses

@app.post("/course")
def add_completed_courses(course:Course):
    db.insert_course()