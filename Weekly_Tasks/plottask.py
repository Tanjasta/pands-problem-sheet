# plottask.py
# This program displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Tatjana Staunton

import numpy as np # Importing numpy
import matplotlib.pyplot as plt # Importing matplot lib

# Generates 1000 random values from a normal distribution with mean 5 and standard deviation 2
values = np.random.normal(5, 2, 1000)

# Creates a histogram of the values
plt.hist(values, bins=50, density=True, alpha=0.5)

# Creating an array of x values in the range [0, 10]
x = np.linspace(0, 10, 100)

# Defines the function h(x) = x^3
def h(x):
    return x**3

# Compute the corresponding y values
y = h(x)
plt.plot(x, y, color='purple') # Plot the function h(x) on the same set of axes and add plot color

# Adds labels and a title
plt.xlabel('value')  # add x-axis label
plt.ylabel('Density') # add y-axis label
plt.title('Histogram and Plot') # add plot title

plt.show() # Shows the plot
