import pandas as pd

df = pd.read_csv('../Data/superstore.csv', encoding='cp1252')

# 1. Clean column names (lowercase and underscores)
df.columns = [c.lower().replace(' ', '_').replace('-', '_') for c in df.columns]
df.rename(columns={'row_labels': 'order_date'}, inplace=True)

df = df[df['order_date'] != 'Grand Total']
df = df[df['ship_date'] != 'Grand Total']


# 2. Convert dates
df['order_date'] = pd.to_datetime(df['order_date'], format='mixed')
df['ship_date'] = pd.to_datetime(df['ship_date'], format='mixed')

# 3. Export to a 'Clean' version for Excel
df.to_csv('../Data/superstore_cleaned.csv', index=False)