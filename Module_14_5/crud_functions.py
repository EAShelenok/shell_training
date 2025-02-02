import sqlite3

connection = sqlite3.connect('bot_dbase.db')
cursor = connection.cursor()

def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOt NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')
    connection.commit()

def get_all_products():
    find_products = cursor.execute("SELECT * FROM Products")
    connection.commit()
    return find_products

def add_user(username, email, age):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
                   (f"{username}", f"{email}", f"{age}", 1000))
    connection.commit()

def is_uncluded(username):
    users = cursor.execute("SELECT * FROM Users WHERE username = ?", (f"{username}",))
    if users.fetchone() is None:
        #connection.commit()
        return False
    else:
        #connection.commit()
        return True