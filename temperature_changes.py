""" 2.Visualize the daily temperature changes over time in a city and give your conclusion

 Input: days = list(range(1, 32)) 

# Daily temperature data (replace with your own data) 

temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]"""

import matplotlib.pyplot as plt

# Data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', color='orange', linestyle='-', linewidth=2, markersize=6)
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')
plt.title('Daily Temperature Changes Over a Month')
plt.grid(True)

# Show the chart
plt.show()
