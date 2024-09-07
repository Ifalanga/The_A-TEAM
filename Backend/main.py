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

    user.password = str(hashed_password.decode('utf-8'))
    print(user.password)
    db.insert_user(user)

    return {"message": "User added successfully"}

@app.get("/user/{user_name}")
def get_user(username: str):
    user = db.get_user(username)

    if user is None:
        raise HTTPException(status_code=404, detail="The user was not found")

    return user


@app.put("/username")
def update_user(user: User, username:str):
    if username != user.username:
        raise HTTPException(status_code=400, detail="Username in path and request body do not match.")

    success = db.update_user(user)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or update failed")

    return {"message": "User updated successfully"}

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
    if not db.insert_course(course):
        raise HTTPException(status_code=500, detail="adding the course failed")
    else:
        return {"message": "Course added successfully"}


