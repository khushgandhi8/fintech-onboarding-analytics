import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

# Pull user signup dates
cursor.execute("SELECT user_id, signup_date FROM users")
users = cursor.fetchall()

BANK_LINK_SUCCESS_RATE = 0.35

for user_id, signup_date_str in users:
    signup_date = datetime.strptime(signup_date_str, "%Y-%m-%d")

    # Bank link attempt happens within 0-3 days after signup
    link_date = signup_date + timedelta(days=random.randint(0, 3))

    link_success = 1 if random.random() < BANK_LINK_SUCCESS_RATE else 0

    cursor.execute("""
        INSERT INTO bank_links (user_id, link_date, link_success)
        VALUES (?, ?, ?)
    """, (user_id, link_date.strftime("%Y-%m-%d"), link_success))

conn.commit()
conn.close()

print("Bank link simulation complete.")
