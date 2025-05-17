#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Create the figure with a 3x2 grid
fig = plt.figure(figsize=(12, 8))
fig.suptitle('All in One', fontsize='medium')

# First plot (y = x^3)
ax0 = plt.subplot(3, 2, 1)
ax0.plot(np.arange(0, 11), y0, 'r-')
ax0.set_xlim(0, 10)
ax0.set_ylim(0, 1000)
ax0.tick_params(labelsize='x-small')

# Second plot (Height vs Weight scatter)
ax1 = plt.subplot(3, 2, 2)
ax1.scatter(x1, y1, color='magenta', s=5)
ax1.set_title("Men's Height vs Weight", fontsize='x-small')
ax1.set_xlabel('Height (in)', fontsize='x-small')
ax1.set_ylabel('Weight (lbs)', fontsize='x-small')
ax1.set_xlim(55, 80)
ax1.set_ylim(165, 195)
ax1.tick_params(labelsize='x-small')

# Third plot (C-14 decay with log scale)
ax2 = plt.subplot(3, 2, 3)
ax2.semilogy(x2, y2, 'b-')
ax2.set_title('Exponential Decay of C-14', fontsize='x-small')
ax2.set_xlabel('Time (years)', fontsize='x-small')
ax2.set_ylabel('Fraction Remaining', fontsize='x-small')
ax2.set_xlim(0, 28650)
ax2.tick_params(labelsize='x-small')

# Fourth plot (Two radioactive decays)
ax3 = plt.subplot(3, 2, 4)
ax3.plot(x3, y31, 'r--', label='C-14')
ax3.plot(x3, y32, 'g-', label='Ra-226')
ax3.set_title('Exponential Decay of Radioactive Elements', fontsize='x-small')
ax3.set_xlabel('Time (years)', fontsize='x-small')
ax3.set_ylabel('Fraction Remaining', fontsize='x-small')
ax3.set_xlim(0, 20000)
ax3.set_ylim(0, 1)
ax3.legend(loc='upper right', fontsize='x-small')
ax3.tick_params(labelsize='x-small')

# Fifth plot (histogram spanning two columns)
ax4 = plt.subplot(3, 2, (5, 6))
bins = np.arange(0, 101, 10)
ax4.hist(student_grades, bins=bins, edgecolor='black', color='#1f77b4')
ax4.set_title('Project A', fontsize='x-small')
ax4.set_xlabel('Grades', fontsize='x-small')
ax4.set_ylabel('Number of Students', fontsize='x-small')
ax4.set_xlim(0, 100)
ax4.set_ylim(0, 30)
ax4.tick_params(labelsize='x-small')

# Adjust layout
plt.tight_layout()
plt.subplots_adjust(top=0.9)  # Make room for the figure title
plt.show()