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
    connection.commit()

def get_all_products():
    find_products = cursor.execute("SELECT * FROM Products")
    connection.commit()
    return find_products