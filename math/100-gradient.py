#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)

x = np.random.randn(2000) * 10
y = np.random.randn(2000) * 10
z = np.random.rand(2000) + 40 - np.sqrt(np.square(x) + np.square(y))

# Create the figure
plt.figure(figsize=(10, 6))

# Create the scatter plot with color mapped to elevation
scatter = plt.scatter(x, y, c=z, cmap='viridis', marker='o', alpha=0.8)

# Set the axis labels
plt.xlabel('x coordinate (m)')
plt.ylabel('y coordinate (m)')

# Set the title
plt.title('Mountain Elevation')

# Set axis limits to match the image
plt.xlim(-40, 40)
plt.ylim(-40, 40)

# Add a colorbar and label it
cbar = plt.colorbar(scatter)
cbar.set_label('elevation (m)')

# Display the plot
plt.tight_layout()
plt.show()