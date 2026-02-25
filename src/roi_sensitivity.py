import sqlite3

DB = "data/fintech.db"

ARPU_VALUES = [10, 20, 30, 40, 50]     # revenue per depositor per year
BONUS_VALUES = [0, 1, 2, 3, 4, 5]      # $ bonus paid per eligible depositor

conn = sqlite3.connect(DB)
cursor = conn.cursor()

# Pull overall depositors by variant (overall first deposit counts)
cursor.execute("""
SELECT
  ea.variant,
  COUNT(DISTINCT u.user_id) AS users,
  SUM(CASE WHEN d.deposit_success = 1 THEN 1 ELSE 0 END) AS depositors
FROM users u
JOIN experiment_assignments ea ON u.user_id = ea.user_id
LEFT JOIN deposits d ON u.user_id = d.user_id
WHERE ea.experiment_name = 'onboarding_bonus_test'
GROUP BY ea.variant
""")
rows = cursor.fetchall()
stats = {variant: {"users": int(n), "depositors": int(x)} for variant, n, x in rows}

control_depositors = stats["control"]["depositors"]
treat_depositors = stats["treatment"]["depositors"]
incremental_depositors = treat_depositors - control_depositors

# Count eligible bonus recipients under TARGETED policy:
# treatment + paid acquisition + successful depositor
cursor.execute("""
SELECT COUNT(*)
FROM users u
JOIN experiment_assignments ea ON u.user_id = ea.user_id
JOIN deposits d ON u.user_id = d.user_id
WHERE ea.experiment_name='onboarding_bonus_test'
  AND ea.variant='treatment'
  AND u.acquisition_channel='paid'
  AND d.deposit_success=1
""")
eligible_paid_treatment_depositors = int(cursor.fetchone()[0])

conn.close()

print("=== Observed counts (current run) ===")
print(f"Control depositors:   {control_depositors}")
print(f"Treatment depositors: {treat_depositors}")
print(f"Incremental depositors (treat - control): {incremental_depositors}")
print(f"Eligible bonus recipients (paid + treatment + depositor): {eligible_paid_treatment_depositors}")

print("\n=== ROI Sensitivity (Targeted bonus policy) ===")
print("Rows: ARPU, Columns: Bonus. Values: Net impact ($)")
print("Net impact = (incremental_depositors * ARPU) - (eligible_bonus_recipients * Bonus)")

# header
header = "ARPU\\BONUS | " + " | ".join([f"{b:>4}" for b in BONUS_VALUES])
print(header)
print("-" * len(header))

for arpu in ARPU_VALUES:
    nets = []
    for bonus in BONUS_VALUES:
        net = (incremental_depositors * arpu) - (eligible_paid_treatment_depositors * bonus)
        nets.append(f"{net:>4}")
    print(f"{arpu:>9} | " + " | ".join(nets))

# Break-even bonus for a given ARPU (max bonus that keeps net >= 0)
print("\n=== Break-even bonus (max $ bonus to keep net >= 0) by ARPU ===")
for arpu in ARPU_VALUES:
    if eligible_paid_treatment_depositors == 0:
        print(f"ARPU={arpu}: no eligible recipients (cost=0)")
        continue
    max_bonus = (incremental_depositors * arpu) / eligible_paid_treatment_depositors
    print(f"ARPU={arpu}: max_bonus ≈ ${max_bonus:.2f}")