import sqlite3
import random
from datetime import datetime, timedelta

conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

# Clear existing deposits table
cursor.execute("DELETE FROM deposits")

# Get linked users + experiment + acquisition channel
cursor.execute("""
SELECT u.user_id, u.signup_date, ea.variant, u.acquisition_channel, bl.link_date
FROM users u
JOIN bank_links bl ON u.user_id = bl.user_id
JOIN experiment_assignments ea ON u.user_id = ea.user_id
WHERE bl.link_success = 1
  AND ea.experiment_name = 'onboarding_bonus_test'
""")

linked_users = cursor.fetchall()

BASELINE_RATE = 0.50
BONUS_RATE = 0.60

for user_id, signup_date_str, variant, channel, link_date_str in linked_users:
    link_date = datetime.strptime(link_date_str, "%Y-%m-%d")

    if variant == "control":
        p = BASELINE_RATE
    else:
        # treatment
        if channel == "paid":
            p = BONUS_RATE
        else:
            p = BASELINE_RATE

    deposit_success = 1 if random.random() < p else 0
    deposit_date = link_date + timedelta(days=random.randint(0, 7))
    amount = round(random.uniform(10, 200), 2) if deposit_success else 0.0

    cursor.execute("""
        INSERT INTO deposits (user_id, deposit_date, amount, deposit_success)
        VALUES (?, ?, ?, ?)
    """, (user_id, deposit_date.strftime("%Y-%m-%d"), amount, deposit_success))

conn.commit()
conn.close()

print("Targeted deposit simulation complete.")