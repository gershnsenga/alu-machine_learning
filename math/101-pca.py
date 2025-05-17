#!/usr/bin/env python3
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

lib = np.load("pca.npz.zip")
data = lib["data"]
labels = lib["labels"]

data_means = np.mean(data, axis=0)
norm_data = data - data_means
_, _, Vh = np.linalg.svd(norm_data)
pca_data = np.matmul(norm_data, Vh[:3].T)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Get unique labels (0, 1, 2) for the three Iris species
unique_labels = np.unique(labels)

# Define colors for each species using plasma colormap
colors = plt.cm.plasma(np.linspace(0, 1, len(unique_labels)))

# Plot each species with a different color
for i, label in enumerate(unique_labels):
    # Get indices for the current species
    indices = np.where(labels == label)
    
    # Plot the data points for this species
    ax.scatter(
        pca_data[indices, 0],     # U1 dimension
        pca_data[indices, 1],     # U2 dimension
        pca_data[indices, 2],     # U3 dimension
        c=[colors[i]],            # Color for this species
        label=f'Class {label}',    # Label for legend
        alpha=0.8,                # Slight transparency
        s=40                      # Point size
    )

# Set axis labels
ax.set_xlabel('U1')
ax.set_ylabel('U2')
ax.set_zlabel('U3')

# Set title
plt.title('PCA of Iris Dataset')

# Set a grid for better visualization
ax.grid(True)

# Adjust the viewing angle to match the image
ax.view_init(elev=30, azim=-45)

# Display the plot
plt.tight_layout()
plt.show()