import csv
import math

# Define your function here
def func(x):
    return 7 / (1 + math.exp(-5 * x))

# Settings
start = -20
end = 20
step = 0.05
filename = "./Quiz1/data.csv"

# Generate x and y values
x_values = [start + i * step for i in range(int((end - start) / step) + 1)]
y_values = [func(x) for x in x_values]

# Write to CSV
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["x", "y"])  # Header
    for x, y in zip(x_values, y_values):
        writer.writerow([x, y])

print(f"CSV file '{filename}' has been created.")