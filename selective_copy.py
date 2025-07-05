import json
import sqlite3
import pandas as pd

with open("../config/selective_tables.json") as f:
    config = json.load(f)

src = sqlite3.connect("source.db")
dest = sqlite3.connect("destination_selective.db")

for table, columns in config.items():
    cols_str = ", ".join(columns)
    df = pd.read_sql(f"SELECT {cols_str} FROM {table}", src)
    df.to_sql(table, dest, if_exists="replace", index=False)

print("Selective data copied.")

