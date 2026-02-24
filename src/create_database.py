import sqlite3

# Create database file
conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

# Load schema
with open("sql/schema.sql", "r") as f:
    schema = f.read()

cursor.executescript(schema)

conn.commit()
conn.close()

print("Database created successfully.")
