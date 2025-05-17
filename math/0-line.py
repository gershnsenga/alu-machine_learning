#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot the line graph
plt.figure(figsize=(10, 6))
plt.plot(np.arange(0, 11), y, color='red', linewidth=2)

# Set the axis limits
plt.xlim(0, 10)
plt.ylim(0, 1000)

# Add grid and labels if needed (optional)
plt.grid(False)

# Display the plot
plt.show()
