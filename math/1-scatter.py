#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

mean = [69,0]
cov = [[15,8], [8,15]]
np.random.seed(5)
x,y= np.random.multivariate_normal(mean, cov, 2000).T
y +=180

#  create the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(x,y,color="magenta", alpha=0.8, s=10)

#  set the axis labels
plt.xlabel("Height (in)")
plt.ylabel("Weight (lbs)")

#  set the title
plt.title("Men's Height vs Weight")

# Adjust the axes limits to match the image
plt.xlim(55, 80)
plt.ylim(165, 195)

# Display the plot
plt.tight_layout()
plt.show()
