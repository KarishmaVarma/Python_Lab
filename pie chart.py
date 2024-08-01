"""1. Create a pie chart to visualize the distribution of your monthly income by source. You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.

 Input: income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] 

monthly_income = [5000, 1500, 1000, 600, 400]
"""
import matplotlib.pyplot as plt

# Data provided
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create pie chart
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0'])
plt.title('Monthly Income Distribution by Source')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Show the pie chart
plt.show()
