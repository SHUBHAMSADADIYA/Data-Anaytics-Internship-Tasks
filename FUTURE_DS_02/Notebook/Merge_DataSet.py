import pandas as pd

# Load datasets
accounts = pd.read_csv('../Data/ravenstack_accounts.csv')
subs = pd.read_csv('../Data/ravenstack_subscriptions.csv')
churn = pd.read_csv('../Data/ravenstack_churn_events.csv')

# Merge to see who is still active vs. who churned
df = accounts.merge(subs, on='account_id', how='left')
df = df.merge(churn, on='account_id', how='left')

# Create a 'Status' column: 1 if churn_date exists, else 0
df['is_churned'] = df['churn_date'].notnull().astype(int)

# Save the merged dataset
df.to_csv('../Data/ravenstack_merged.csv', index=False)