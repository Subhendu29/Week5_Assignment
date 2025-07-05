import sqlite3
import pandas as pd

src = sqlite3.connect("source.db")
dest = sqlite3.connect("destination.db")

cur = src.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cur.fetchall()]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", src)
    df.to_sql(table, dest, if_exists="replace", index=False)

print("All tables copied.")

