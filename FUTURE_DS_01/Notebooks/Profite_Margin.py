import pandas as pd

# Load your dataset
df = pd.read_csv('../Data/Task-1/superstore_cleaned.csv')

# Create the Profit Margin column
# We multiply by 100 to get a percentage (e.g., 0.25 becomes 25.0)
df['profit_margin'] = (df['profit'] / df['sales']) * 100

# Optional: Round to 2 decimal places for a cleaner look
df['profit_margin'] = df['profit_margin'].round(2)

# Save the updated file
df.to_csv('../Data/Task-1/superstore_data.csv', index=False)