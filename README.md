# Fintech Onboarding: A/B Test & Incentive ROI Analysis

**Does a $5 first-deposit bonus improve onboarding conversion — and is it worth it?**

This project simulates a 10,000-user fintech onboarding funnel to answer that question using A/B testing, funnel analysis, segmentation, and unit economics modeling.

📊 **[View Live Dashboard →](https://khushgandhi8.github.io/fintech-onboarding-analytics/)**

---

## The Problem

A personal finance app offers users a $5 cash bonus to make their first deposit within 7 days of signup. The product team wants to know: does it actually move the needle, and does the math work out?

The funnel has three steps: **signup → bank link → first deposit**. The north star metric is **first deposit rate within 7 days**.

---

## What I Found

The bonus works statistically — but fails on unit economics.

| Variant | First Deposit Rate | Lift | p-value |
|---|---|---|---|
| Control (no bonus) | 18.0% | — | — |
| Treatment ($5 blanket bonus) | 22.1% | +4.12pp | <1e-6 |
| Targeted (paid channel only) | 19.46% | +1.46pp | 0.062 |

The blanket bonus produces a highly significant lift, but at ARPU = $20, the cost of the bonus exceeds the incremental revenue it generates — **negative ROI**. The break-even bonus amount is **$3.48**, and the break-even ARPU for the $5 bonus is **~$30**.

The biggest leak in the funnel isn't the deposit step — it's **bank linking**, where 64.4% of users drop off. This is likely a UX problem, not an incentive problem.

---

## Recommendation

1. **Don't roll out the $5 blanket bonus.** Statistically significant ≠ economically justified.
2. **Test a $3 bonus targeted to paid-channel users**, who show the highest baseline intent (~23% deposit rate).
3. **Prioritize fixing the bank-link drop-off.** A 10pp improvement there would outperform any deposit incentive at zero marginal cost.
4. **Invest in post-deposit retention** to raise ARPU toward $30+, at which point the $5 bonus becomes profitable.

---

## Segmentation Highlights

- **Working professionals** convert at ~24% vs. ~14% for students — nearly 2x the rate
- **Paid-channel users** are the highest-intent segment and the best target for any incentive
- Device type (iOS vs. Android) showed minimal difference

---

## Project Structure

```
├── data/               # Simulated SQLite database (10k users)
├── notebooks/          # Analysis notebook with visualizations
├── sql/                # Queries for funnel metrics and experiment results
├── src/                # Data generation and analysis scripts
├── docs/               # Live dashboard (index.html) and decision memo
└── README.md
```

---

## Stack

Python · SQLite · pandas · matplotlib · HTML/CSS/JS

---

## Skills Demonstrated

Experimental design · Statistical hypothesis testing · Funnel analysis · Cohort segmentation · Unit economics modeling · Data visualization · Business recommendation framing