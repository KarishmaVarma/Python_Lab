""" 1.Create a bar chart to represent monthly expenses in different spending categories and give your conclusion. 

Input: categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation'] 

# Monthly expenses in dollars (replace with your own data) 

expenses = [1200, 400, 200, 150, 250]"""


import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color='skyblue')
plt.xlabel('Category')
plt.ylabel('Expenses ($)')
plt.title('Monthly Expenses by Category')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the chart
plt.show()
