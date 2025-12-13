"""
Program Name: lab16_ssrinivasan3-2.py

Author: Shrrayash Srinivasan

Purpose: 

Date: December 12, 2025 
"""

"""Will be added shortly"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('OHUR.csv')

# Print header info using enumerate
for i, col in enumerate(df.columns):
    print(f"{i}: {col}")

# Convert DATE column to datetime
df['DATE'] = pd.to_datetime(df['DATE'])

# Plot the graph
plt.figure(figsize=(12, 6))
plt.plot(df['DATE'], df['OHUR'], color='red', linewidth=1.5)
plt.title('Ohio Unemployment Rate by Month (1976–2022)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.tight_layout()
plt.show()  

