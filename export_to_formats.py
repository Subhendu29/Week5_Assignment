import pandas as pd
import sqlite3
import pyarrow as pa
import pyarrow.parquet as pq
import fastavro

conn = sqlite3.connect("source.db")
df = pd.read_sql("SELECT * FROM users", conn)

# CSV
df.to_csv("../data/csv/users.csv", index=False)

# Parquet
table = pa.Table.from_pandas(df)
pq.write_table(table, "../data/parquet/users.parquet")

# Avro
records = df.to_dict(orient='records')
schema = {
    "type": "record",
    "name": "User",
    "fields": [{"name": col, "type": "string"} for col in df.columns]
}
with open("../data/avro/users.avro", "wb") as out:
    fastavro.writer(out, schema, records)

