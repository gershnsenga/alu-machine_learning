#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create the figure
plt.figure(figsize=(10, 6))

# Create the histogram
bins = np.arange(0, 101, 10)  # Create bins from 0 to 100 with step 10
plt.hist(student_grades, bins=bins, edgecolor='black', color='#1f77b4')

# Set axis labels
plt.xlabel('Grades')
plt.ylabel('Number of Students')

# Set title
plt.title('Project A')

# Set x-axis range to match the image (0 to 100)
plt.xlim(0, 100)

# Set y-axis range to match the image (0 to 30)
plt.ylim(0, 30)

# Display the plot
plt.tight_layout()
plt.show()