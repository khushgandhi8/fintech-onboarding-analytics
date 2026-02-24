import sqlite3
import random
from datetime import datetime

conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

cursor.execute("SELECT user_id, signup_date FROM users")
users = cursor.fetchall()

for user in users:
    user_id = user[0]
    signup_date = user[1]

    variant = random.choice(["control", "treatment"])

    cursor.execute("""
        INSERT INTO experiment_assignments (user_id, experiment_name, variant, assignment_time)
        VALUES (?, ?, ?, ?)
    """, (
        user_id,
        "onboarding_bonus_test",
        variant,
        signup_date
    ))

conn.commit()
conn.close()

print("Experiment assignments completed.")
