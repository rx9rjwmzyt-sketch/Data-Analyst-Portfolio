import pandas as pd
import numpy as np

# 1. The Dirty Data
data = {
    'Transaction_ID': [101, 102, 103, 103, 104, 105], 
    'Branch': ['London', 'Manchester', 'London', 'London', 'Lndn', 'Manchester'],
    'Date': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
    'Revenue': [500, 450, 600, 600, np.nan, 480], 
    'Profit': [150, 120, 180, 180, 20, np.nan]
}
df = pd.DataFrame(data)

print("--- 1. Original Dirty Data ---")
print(df)

# ---------------------------------------------------------
# THE CLEANING PHASE
# ---------------------------------------------------------

# Fix #1: Remove Duplicates
# We tell Python: "If a row is identical to another, delete it."
df = df.drop_duplicates()

# Fix #2: Fix Typos
# We tell Python: "Find 'Lndn' and replace it with 'London'."
df['Branch'] = df['Branch'].replace('Lndn', 'London')

# Fix #3: Handle Missing Numbers (NaN)
# Strategy: Fill missing Revenue with the Average (Mean) Revenue of the shop
mean_revenue = df['Revenue'].mean()
df['Revenue'] = df['Revenue'].fillna(mean_revenue)

# For Profit, let's just assume it's 0 if missing (Conservative approach)
df['Profit'] = df['Profit'].fillna(0)

# ---------------------------------------------------------

print("\n--- 2. Sparkly Clean Data ---")
print(df)