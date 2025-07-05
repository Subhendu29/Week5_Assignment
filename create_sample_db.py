import sqlite3

conn = sqlite3.connect("source.db")
cur = conn.cursor()

cur.execute("CREATE TABLE users (id INTEGER, name TEXT, email TEXT)")
cur.execute("CREATE TABLE orders (id INTEGER, user_id INTEGER, amount REAL)")

cur.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, 'Alice', 'alice@example.com'),
    (2, 'Bob', 'bob@example.com')
])
cur.executemany("INSERT INTO orders VALUES (?, ?, ?)", [
    (1, 1, 100.5),
    (2, 2, 200.0)
])

conn.commit()
conn.close()
