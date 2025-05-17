#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4,3))

# Create the figure
plt.figure(figsize=(10, 6))

# Set up the people (x-axis) and fruit types with their colors
people = ['Farrah', 'Fred', 'Felicia']
fruit_types = ['apples', 'bananas', 'oranges', 'peaches']
colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  # red, yellow, orange, peach

# Create a range for the x-axis positions
x = np.arange(len(people))

# Initialize the bottom position for stacking
bottom = np.zeros(3)

# Create the stacked bar chart
for i, (fruit_type, color) in enumerate(zip(fruit_types, colors)):
    plt.bar(x, fruit[i], bottom=bottom, width=0.5, label=fruit_type, color=color)
    bottom += fruit[i]

# Set the x-axis ticks and labels
plt.xticks(x, people)

# Set the y-axis label and range
plt.ylabel('Quantity of Fruit')
plt.ylim(0, 80)
plt.yticks(np.arange(0, 81, 10))

# Set the title
plt.title('Number of Fruit per Person')

# Add the legend
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()