import sqlite3
import os

DB_PATH = "data/fintech.db"

# Delete old db file to start fresh
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

with open("sql/schema.sql", "r") as f:
    schema = f.read()

cursor.executescript(schema)

conn.commit()
conn.close()

print("Fresh database created successfully.")