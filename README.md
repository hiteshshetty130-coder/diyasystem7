## Project Overview:-
The project implements a python based billing engine for a subscription based digital service. It Processes subscription and usage data to calculate monthly charges, final status, and  generate billing output and perform tests using unittest

## Workflow
Load Data → Aggregate Usage → Calculate Bill → Evaluate Status → Generate Reports → Run Tests


## Business rules:-
1. USAGE AGGREGATION
- Aggregate total data usage per subscription for the given month
- Ignore usage records with invalid dates

2. BILLING RULES
- If usage <= usage_limit_gb → total bill = monthly_fee
- If usage > usage_limit_gb:
    overage_gb = usage - usage_limit_gb
    overage_charge = overage_gb * 10
    total bill = monthly_fee + overage_charge
- If status = SUSPENDED → bill only monthly_fee (no overage)
- If status = CANCELLED → bill = 0

3. STATUS EVALUATION RULES
- If usage > 150% of usage_limit_gb → final_status = SUSPENDED
- If previous status was SUSPENDED and usage <= limit → final_status = ACTIVE
- CANCELLED status must never change


## How to run the Application:-
from the project root:
python src/main.py

this generates---- billing_output.csv , billing_summary.json , logs/billing.log

## How to run the Unittest:-
python -m unittest discover

## Assumptions made:-
1) The missing usage records and implify usage=0
2) First Aggregation are calculated then billing calculation and then status calculation
3) The output csv files contains all the required columns 
4) Billing json file contains all the metrics which was required 

## Edge cases handled:-
1) Empty usage files 
2) invalid dates are skipped
3) Cancelled subscriptions
4) suspended subscriptions
5) over the limit data usage are handled and calculated 





