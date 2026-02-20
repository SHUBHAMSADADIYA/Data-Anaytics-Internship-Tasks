import pandas as pd

# Load accounts data
accounts = pd.read_csv('d:/DA Tasks/Tasks/Task-2/Data/ravenstack_accounts.csv')
print("Accounts columns:", accounts.columns.tolist())

# Load subscriptions data
subs = pd.read_csv('d:/DA Tasks/Tasks/Task-2/Data/ravenstack_subscriptions.csv')
print("Subs columns:", subs.columns.tolist())
print(f"Subs rows: {len(subs)}")
print(f"Unique account_ids in subs: {subs['account_id'].nunique()}")

# Merge
master_df = accounts.merge(subs, on='account_id', how='left')
print("Master DF columns:", master_df.columns.tolist())
print(f"Master DF rows: {len(master_df)}")

# Check duplicates
if len(master_df) > len(accounts):
    print("WARNING: Merge resulted in row expansion (duplicates).")
