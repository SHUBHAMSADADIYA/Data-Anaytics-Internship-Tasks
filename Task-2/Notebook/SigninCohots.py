import pandas as pd

# Load accounts data
accounts = pd.read_csv('../Data/ravenstack_accounts.csv')

# Convert to datetime and create the 'Signup Month' column
accounts['signup_date'] = pd.to_datetime(accounts['signup_date'])
accounts['signup_cohort'] = accounts['signup_date'].dt.to_period('M')

# Merge accounts with subscriptions to get the plan level
subs = pd.read_csv('../Data/ravenstack_subscriptions.csv')
master_df = accounts.merge(subs, on='account_id', how='left')

# Group by cohort and plan level
cohort_plan = accounts.groupby(['signup_cohort', 'plan_tier']).size().reset_index(name='count')
# Save the cohort plan data
cohort_plan.to_csv('../Data/cohort_plan.csv', index=True)
