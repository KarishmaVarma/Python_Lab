"""1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])"""

import numpy as np

# Modified temperature readings to include cold days
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4.0, -4.0, -12.0])

# Identifying hot and cold days
hot_days = np.where(temperatures > 35)[0]
cold_days = np.where(temperatures < 5)[0]

# Formatting output
output = "Hot Days:\nDay    Temperature (°C)\n"
for day in hot_days:
    output += f"{day + 1}      {temperatures[day]}\n"

output += "\nCold Days:\nDay    Temperature (°C)\n"
for day in cold_days:
    output += f"{day + 1}      {temperatures[day]}\n"

print(output)

"""
Output:
Hot Days:
Day    Temperature (°C)
3      36.8
6      38.7
10      37.2

Cold Days:
Day    Temperature (°C)
11      4.0
12      -4.0
13      -12.0"""
