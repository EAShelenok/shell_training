import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        age INTEGER,
        balance INTEGER NOT NULL
        )
''')
#Код решения предыдущей задачи

#db_st = 10 #Зададим количество записей в таблице
#for st in range(db_st):
#    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)",
#                   (f'User{st + 1}', f'example{st + 1}@gmail.com', 10 * (st + 1), 1000))
#
#cursor.execute(f"UPDATE Users SET balance = ? WHERE id IN {str(tuple([i for i in range(1, db_st + 1, 2)]))}",
#              (500,))
#
#cursor.execute(f"DELETE FROM Users WHERE id IN {str(tuple([i for i in range(1, db_st + 1, 3)]))}")
#
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age <> 60")
#find_users = cursor.fetchall()
#
#for item in find_users:
#    print(f"Имя: {item[0]} | Почта: {item[1]} | Возраст: {item[2]} | Баланс: {item[3]}")

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

print(f"Cредний баланс всех пользователей: {all_balances/total_users}")

connection.commit()
connection.close()