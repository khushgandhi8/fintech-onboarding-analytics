import sqlite3

conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

# Deposit rate among successfully bank-linked users, by variant
cursor.execute("""
SELECT
  ea.variant,
  COUNT(*) AS linked_users,
  SUM(d.deposit_success) AS deposit_successes,
  1.0 * SUM(d.deposit_success) / COUNT(*) AS deposit_rate_given_link
FROM bank_links bl
JOIN experiment_assignments ea ON bl.user_id = ea.user_id
LEFT JOIN deposits d ON bl.user_id = d.user_id
WHERE bl.link_success = 1
  AND ea.experiment_name = 'onboarding_bonus_test'
GROUP BY ea.variant
ORDER BY ea.variant;
""")

print("Deposit rate among bank-linked users:")
for row in cursor.fetchall():
    variant, linked_users, deposit_successes, deposit_rate = row
    print(f"  {variant}: linked={linked_users}, deposit_successes={deposit_successes}, rate={deposit_rate:.4f}")

# Overall first deposit rate out of all signups, by variant
cursor.execute("""
SELECT
  ea.variant,
  COUNT(DISTINCT u.user_id) AS total_users,
  SUM(CASE WHEN d.deposit_success = 1 THEN 1 ELSE 0 END) AS depositors,
  1.0 * SUM(CASE WHEN d.deposit_success = 1 THEN 1 ELSE 0 END) / COUNT(DISTINCT u.user_id) AS first_deposit_rate
FROM users u
JOIN experiment_assignments ea ON u.user_id = ea.user_id
LEFT JOIN deposits d ON u.user_id = d.user_id
WHERE ea.experiment_name = 'onboarding_bonus_test'
GROUP BY ea.variant
ORDER BY ea.variant;
""")

print("\nOverall first deposit rate (out of all signups):")
for row in cursor.fetchall():
    variant, total_users, depositors, rate = row
    print(f"  {variant}: users={total_users}, depositors={depositors}, rate={rate:.4f}")

conn.close()
