#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 28651, 5730)
r = np.log(0.5)
t = 5730
y = np.exp((r / t) * x)

# Create the figure and plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, color='#1f77b4')  # Using the blue color from the image

# Set the axis labels
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')

# Set the title
plt.title('Exponential Decay of C-14')

# Set the y-axis to logarithmic scale
plt.yscale('log')

# Set the x-axis range
plt.xlim(0, 28650)

# Set the y-axis limits to match the image (from about 0.03 to 1.0)
plt.ylim(0.025, 1.0)

# Display the plot
plt.grid(False)
plt.tight_layout()
plt.show()