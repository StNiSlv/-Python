import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users = [(i, f"User{i}", f"example{i}@gmail.com", i * 10, 1000) for i in range(1, 11)]
cursor.executemany('INSERT OR IGNORE INTO Users VALUES (?, ?, ?, ?, ?)', users)

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 != 0')

cursor.execute('SELECT id FROM Users')
id_to_delete = [row[0] for row in cursor.fetchall()][::3]
cursor.execute(f'DELETE FROM Users WHERE id IN ({",".join(map(str, id_to_delete))})')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
for row in cursor.fetchall():
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")
cursor.execute("DELETE FROM Users WHERE id = 6")

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

average_balance = all_balances / total_users
print(average_balance)
conn.commit()
conn.close()