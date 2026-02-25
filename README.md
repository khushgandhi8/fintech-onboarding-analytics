# Fintech Onboarding Experiment & Incentive Optimization

This project simulates a fintech onboarding funnel (10k users) to evaluate a $5 first-deposit incentive using A/B testing, statistical inference, and unit economics modeling.

Key findings:
- Blanket bonus increased conversion (+4.1pp, p<1e-6) but produced negative ROI at ARPU=$20.
- Targeted incentive reduced cost but required smaller bonus (~$3.50) or higher ARPU (~$30) to break even.
- Demonstrates experimental design, segmentation, statistical testing, and business decision modeling.

## Product Overview
This project analyzes onboarding conversion in a personal finance app where users:

1. Sign up
2. Link a bank account
3. Make their first deposit

## Objective
Identify where users drop off in onboarding and evaluate whether a new onboarding flow improves first deposit conversion.

## North Star Metric
First Deposit Rate (within 7 days of signup)

## Funnel Steps
signup → bank_link → first_deposit

## Segments to Analyze
- user_segment (student vs working_professional)
- device_type (iOS vs Android)
- acquisition_channel (organic, paid, referral)

## Experiment
Control: Existing onboarding flow  
Treatment: Improved onboarding flow  

Goal: Increase bank_link_rate and first_deposit_rate

## Event Definitions

- signup: user account successfully created
- bank_link: user successfully links bank account
- first_deposit: user's first successful deposit transaction within 7 days of signup

## Assumptions

- Users must complete bank_link before making a deposit.
- Deposits can fail due to insufficient funds or verification issues.
- Only successful deposits count toward first_deposit_rate.
- First Deposit Rate is calculated as:
  (# users with successful first_deposit within 7 days) / (# total signups)


## Results:
- Baseline: bank-link ≈ 35.6%, control deposit-after-link ≈ 50.6%
- Blanket bonus: +4.12pp lift, p<1e-6, but negative ROI (cost > revenue)
- Targeted bonus (paid only): +1.46pp lift, p=0.062, lower cost, still negative ROI at ARPU=$20
- Sensitivity: break-even bonus at ARPU=$20 ≈ $3.48
- Recommendation: test $3 bonus targeted to paid OR optimize post-deposit retention to raise ARPU to ~$30+
