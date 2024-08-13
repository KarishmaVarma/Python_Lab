""" Lab 2: Write a Pandas program to create a Pivot table and find the item wise unit sold.

 Input:Download the file salesdata.csv From LMS"""

import pandas as pd
# Load the CSV file
sales_data = pd.read_csv('C:/Users/shaik/Downloads/salesdata.csv')
# Create a pivot table to find the item-wise units sold
pivot_table = pd.pivot_table(
    sales_data,
    values='Units',
    index=['Item'],
    aggfunc='sum'
)
print(pivot_table)



"""Output:
              Units
Item               
Cell Phone      278
Desk             10
Home Theater    722
Television      716
Video Games     395
"""
