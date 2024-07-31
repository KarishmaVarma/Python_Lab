"""2. Calculate the profit made by a company

 Input: revenue = np.array([10000, 12000, 11000, 10500]) 

expenses = np.array([4000, 5000, 4500, 4800])

 Output: Profit: [6000 7000 6500 5700]
 """
import numpy as np

# Input revenue and expenses arrays
revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate profit
profit = revenue - expenses

print("Profit:", profit)

#Output:
#Profit: [6000 7000 6500 5700]
