# plottask.py
# This program displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
# and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.
# Author: Tatjana Staunton


import numpy as np # Imports numpy
import matplotlib.pyplot as plt # Imports matplot lib

values = np.random.normal(5, 2, 1000) # Generates 1000 random values from a normal distribution with mean 5 and standard deviation 2

plt.hist(values, bins=10, alpha=0.5, label='Histogram') # Creates a histogram of the values with 10 bins

x = np.linspace(0, 10, 100) # Creates an array of x values from 0 to 10 with 100 points

y = x**3  # Calculates the y values for the function h(x) = x^3

plt.plot(x, y, 'purple', label='Plot') # Plot the function h(x) on the same set of axes as the histogram

plt.legend() # Adds a legend to the plot

plt.show() # Shows the plot
