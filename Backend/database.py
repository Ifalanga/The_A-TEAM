import sqlite3


from models import User, Course

def create_tables():
    """Create tables in the database if they do not already exist."""
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT NOT NULL PRIMARY KEY,
            fullname TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            interest TEXT NOT NULL,
            level TEXT NOT NULL
        )
        ''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            namecourse TEXT NOT NULL,
            username TEXT NOT NULL,
            FOREIGN KEY(username) REFERENCES users(username)
        )
        ''')
        connection.commit()

def insert_user(user: User):
    """Insert a record into the users table."""
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        print(
            f"Inserting users: {type(user.username)}, {type(user.full_name)}, {type(user.email)}, {type(user.password)}, {type(user.interest)}, {type(user.level)}")
        cursor.execute('''
           INSERT INTO users (username, fullname, email, password, interest, level)
            VALUES (?, ?, ?, ?, ?, ?)

            ''', (user.username, user.full_name, user.email, user.password, user.interest, user.level))
        connection.commit()


def insert_course(course: Course):
    """Insert a record into the courses table."""
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO courses (namecourse, username)
        VALUES (?, ?)
        ''', (course.namecourse, course.username))
        connection.commit()

def get_user(username):
    """Fetch a user by username."""
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        return user

def get_user_courses(username):
    """Fetch all courses associated with a given username."""
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM courses WHERE username = ?', (username,))
        courses_ret = cursor.fetchall()
        return courses_ret

if __name__ == "__main__":
    # Create tables
    create_tables()
    # Add more functionality as needed
