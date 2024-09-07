import sqlite3


from models import User, Course

def create_tables():

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

    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        print(
            f"Inserting users: {type(user.username)}, {type(user.full_name)}, {type(user.email)}, {type(user.password)}, {type(user.interest)}, {type(user.level)}")
        cursor.execute('''
           INSERT INTO users (username, fullname, email, password, interest, level)
            VALUES (?, ?, ?, ?, ?, ?)

            ''', (user.username, user.full_name, user.email, user.password, user.interest, user.level))
        connection.commit()


def update_user(user: User):
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
                   UPDATE users
                   SET fullname = ?, email = ?, password = ?, interest = ?, level = ?
                   WHERE username = ?
               ''', (user.fullname, user.email, user.password, user.interest, user.level, user.username))
        connection.commit()
        if cursor.rowcount == 0:
            return False  # No rows were updated, user might not exist
        return True

def insert_course(course: Course):

    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('''
        INSERT INTO courses (namecourse, username)
        VALUES (?, ?)
        ''', (course.namecourse, course.username))
        connection.commit()
        if cursor.rowcount == 0:
            return False  
        return True

def get_user(username):
    print("hetre")
    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_row = cursor.fetchone()

        if user_row:

            user = User(
                username=user_row[0],
                full_name=user_row[1],
                email=user_row[2],
                password=user_row[3],
                interest=user_row[4],
                level=user_row[5]
            )
            print(f"type pf is:{type(user)}")
            return user

def get_user_courses(username):

    with sqlite3.connect('TheLearningHub_db.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM courses WHERE username = ?', (username,))
        courses_ret = cursor.fetchall()
        return courses_ret

if __name__ == "__main__":
    # Create tables
    create_tables()

