# Fintech Onboarding Funnel Analysis

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

