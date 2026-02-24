import sqlite3
import random
from datetime import datetime, timedelta

# Connect to database
conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

NUM_USERS = 10000

segments = ["student", "working_professional"]
devices = ["iOS", "Android"]
channels = ["organic", "paid", "referral"]

start_date = datetime(2024, 1, 1)

for user_id in range(1, NUM_USERS + 1):
    signup_offset = random.randint(0, 90)
    signup_date = start_date + timedelta(days=signup_offset)

    user_segment = random.choice(segments)
    device_type = random.choice(devices)
    acquisition_channel = random.choice(channels)

    cursor.execute("""
        INSERT INTO users (user_id, signup_date, user_segment, device_type, acquisition_channel)
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        signup_date.strftime("%Y-%m-%d"),
        user_segment,
        device_type,
        acquisition_channel
    ))

conn.commit()
conn.close()

print("Users generated successfully.")
