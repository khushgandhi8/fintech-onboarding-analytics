import sqlite3
import math

def normal_cdf(x: float) -> float:
    # Standard normal CDF using error function
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def two_proportion_z_test(x1: int, n1: int, x2: int, n2: int):
    """
    x1/n1 = control conversion
    x2/n2 = treatment conversion
    Returns z-score and two-sided p-value.
    """
    p1 = x1 / n1
    p2 = x2 / n2
    p_pool = (x1 + x2) / (n1 + n2)

    se = math.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    z = (p2 - p1) / se if se > 0 else float("nan")

    # two-sided p-value
    p_value = 2 * (1 - normal_cdf(abs(z)))
    return p1, p2, z, p_value

def diff_in_proportions_ci(x1: int, n1: int, x2: int, n2: int, z_alpha: float = 1.96):
    """
    95% CI for (p2 - p1) using unpooled standard error.
    """
    p1 = x1 / n1
    p2 = x2 / n2
    se = math.sqrt((p1 * (1 - p1) / n1) + (p2 * (1 - p2) / n2))
    diff = p2 - p1
    lo = diff - z_alpha * se
    hi = diff + z_alpha * se
    return diff, lo, hi

conn = sqlite3.connect("data/fintech.db")
cursor = conn.cursor()

# Get total users and depositors per variant (deposit_success=1)
cursor.execute("""
SELECT
  ea.variant,
  COUNT(DISTINCT u.user_id) AS total_users,
  SUM(CASE WHEN d.deposit_success = 1 THEN 1 ELSE 0 END) AS depositors
FROM users u
JOIN experiment_assignments ea ON u.user_id = ea.user_id
LEFT JOIN deposits d ON u.user_id = d.user_id
WHERE ea.experiment_name = 'onboarding_bonus_test'
GROUP BY ea.variant
""")

rows = cursor.fetchall()
conn.close()

# Map results
stats = {variant: (int(n), int(x)) for variant, n, x in rows}

n_control, x_control = stats["control"]
n_treat, x_treat = stats["treatment"]

p1, p2, z, p_value = two_proportion_z_test(x_control, n_control, x_treat, n_treat)
diff, lo, hi = diff_in_proportions_ci(x_control, n_control, x_treat, n_treat)

print("=== First Deposit Rate (within dataset window) ===")
print(f"Control:   {x_control}/{n_control} = {p1:.4f}")
print(f"Treatment: {x_treat}/{n_treat} = {p2:.4f}")
print(f"Lift (Treatment - Control): {diff:.4f} ({diff*100:.2f} percentage points)")

print("\n=== Two-proportion z-test ===")
print(f"z = {z:.3f}")
print(f"two-sided p-value = {p_value:.6f}")

print("\n=== 95% CI for lift (unpooled) ===")
print(f"[{lo:.4f}, {hi:.4f}]  ->  [{lo*100:.2f}pp, {hi*100:.2f}pp]")

if p_value < 0.05:
    print("\nConclusion: Statistically significant lift at α = 0.05.")
else:
    print("\nConclusion: Lift is NOT statistically significant at α = 0.05.")
