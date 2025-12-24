import pandas as pd
import matplotlib.pyplot as plt

# 1. The Data
data = {
    'Branch': ['London', 'Manchester', 'London', 'London', 'London', 'Manchester'],
    'Revenue': [500, 450, 600, 600, 507.5, 480] 
}
df = pd.DataFrame(data)

# 2. Group the data 
branch_totals = df.groupby('Branch')['Revenue'].sum()
print("--- Data to Plot ---")
print(branch_totals)

# 3. DRAW THE CHART
plt.figure(figsize=(8, 5))

# x-axis = Branch Names, y-axis = Total Revenue
branch_totals.plot(kind='bar', color=['blue', 'orange'])

# Add Labels
plt.title('Total Revenue: London vs Manchester')
plt.ylabel('Revenue ($)')
plt.xlabel('Branch')
plt.xticks(rotation=0) 

# 4. Save the image
plt.savefig('revenue_chart.png')
print("\n✅ Chart saved as 'revenue_chart.png'. Check your file 
list!")