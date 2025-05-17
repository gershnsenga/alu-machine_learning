#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 21000, 1000)
r = np.log(0.5)
t1 = 5730
t2 = 1600
y1 = np.exp((r / t1) * x)
y2 = np.exp((r / t2) * x)

# Create the figure and plot
plt.figure(figsize=(10, 6))

# Plot C-14 with dashed red line
plt.plot(x, y1, 'r--', linewidth=2, label='C-14')

# Plot Ra-226 with solid green line
plt.plot(x, y2, 'g-', linewidth=2, label='Ra-226')

# Set the axis labels
plt.xlabel('Time (years)')
plt.ylabel('Fraction Remaining')

# Set the title
plt.title('Exponential Decay of Radioactive Elements')

# Set the axis ranges
plt.xlim(0, 20000)
plt.ylim(0, 1)

# Add a legend in the upper right corner
plt.legend(loc='upper right')

# Display the plot
plt.grid(False)
plt.tight_layout()
plt.show()