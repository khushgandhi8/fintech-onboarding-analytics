# Fintech Onboarding: A/B Test & Incentive ROI Analysis

I built a simulated 10,000-user fintech onboarding funnel to test whether a $5 first-deposit bonus actually makes sense - statistically and economically. Short answer: it moves conversion, but the unit economics don't hold up at realistic ARPU.

📊 **[Live Dashboard →](https://khushgandhi8.github.io/fintech-onboarding-analytics/)**

---

## Background

A personal finance app wants to increase first deposits by offering new users a $5 cash bonus if they deposit within 7 days of signup. The funnel is simple: signup → bank link → first deposit. The question is whether the bonus pays for itself.

North star metric: **first deposit rate within 7 days of signup**

---

## Results

The bonus works. The ROI doesn't - at least not yet.

| Variant | First Deposit Rate | Lift | p-value |
|---|---|---|---|
| Control | 18.0% | - | - |
| $5 blanket bonus | 22.1% | +4.12pp | <1e-6 |
| $3 targeted (paid channel) | 19.46% | +1.46pp | 0.062 |

At ARPU = $20, the blanket bonus costs more than the incremental revenue it generates. Break-even bonus is **$3.48**; break-even ARPU for the $5 bonus is **~$30**.

One thing that stood out: the biggest drop in the funnel isn't at the deposit step - it's bank linking, where 64.4% of users fall off. That's probably a UX issue, not an incentive issue.

---

## Recommendation

1. Don't ship the $5 blanket bonus. Statistically significant ≠ economically justified.
2. Test a $3 bonus targeted at paid-channel users - they have the highest baseline intent (~23% deposit rate) and make the math closer to working.
3. Look hard at the bank-link drop-off before running more deposit experiments. Fixing that step is free and would likely outperform any bonus.
4. If post-deposit retention improves and ARPU reaches ~$30+, the $5 bonus becomes profitable without any experiment changes.

---

## Segmentation

- Working professionals convert at ~24% vs ~14% for students
- Paid-channel users are the strongest segment for targeting any incentive
- iOS vs Android showed no meaningful difference

---

## Repo Structure

```
├── data/          # Simulated SQLite database (10k users)
├── notebooks/     # Analysis + visualizations
├── sql/           # Funnel and experiment queries
├── src/           # Data generation and analysis scripts
├── docs/          # Dashboard (index.html) and decision memo
```

---

## Stack

Python, SQLite, pandas, matplotlib, HTML/CSS/JS