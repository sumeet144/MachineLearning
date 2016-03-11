# Import libraries
import IPython
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib
import sklearn

# Load Boston data
from sklearn.datasets import load_boston
bdata = load_boston()

# Explore data
print bdata.keys()
print bdata.feature_names
print bdata.data.shape
print bdata.target.shape
# uncomment the following if you want to see a lengthy description of the dataset
print bdata.DESCR

# Prepare IPython to work with matplotlib and import the library to something convenient
%matplotlib inline  
import matplotlib.pyplot as plt  

# Plot histogram of median housing prices
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.hist(bdata.target, facecolor='g', edgecolor='white', bins=50)

# Remove top and right axes
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

# Remove unneeded ticks 
ax.get_xaxis().tick_bottom()  
ax.get_yaxis().tick_left()

# Setting outward ticks on x and y axes
ax.tick_params(axis='both', direction='out')

# Title and labeling
plt.title("Median Housing Prices in Boston\n\n", fontweight='bold')
plt.xlabel("Median Prices in $1000's", fontweight='bold')
plt.ylabel("Count for Houses", fontweight='bold')

# Set y-axis to median housing prices
y = bdata.target
# Set x-axis to per capita crime rate
x = bdata.data[:,0]

# Plot scatter plot
scat = plt.figure()
bx = scat.add_subplot(111)

plt.scatter(x,y, color='m')

# Remove top and right axes
bx.spines["right"].set_visible(False)
bx.spines["top"].set_visible(False)

# Remove unneeded ticks 
bx.get_xaxis().tick_bottom()  
bx.get_yaxis().tick_left()

# Setting outward ticks on x and y axes
bx.tick_params(axis='both', direction='out')

# Title and labeling
plt.title("\nMedian Housing Prices VS per-capita crime rate\n in Boston\n", fontweight='bold')
plt.xlabel("\nPer-capita crime rate", fontweight='bold')
plt.ylabel("Median Housing Prices\n", fontweight='bold')

plt.show()

# Scatter plot for median housing prices with average number of rooms
# Set y-axis to median housing prices
yaxis = bdata.target
# Set x-axis to per capita crime rate
xaxis = bdata.data[:,5]

# Plot scatter plot
graph = plt.figure()
cx = graph.add_subplot(111)

plt.scatter(xaxis,yaxis, color='g')

# Remove top and right axes
cx.spines["right"].set_visible(False)
cx.spines["top"].set_visible(False)

# Remove unneeded ticks 
cx.get_xaxis().tick_bottom()  
cx.get_yaxis().tick_left()

# Setting outward ticks on x and y axes
cx.tick_params(axis='both', direction='out')

# Title and labeling
plt.title("\nRelationship between RM and Price\n", fontweight='bold')
plt.xlabel("\nAverage number of rooms per dwelling (RM)", fontweight='bold')
plt.ylabel("Housing Price\n", fontweight='bold')

plt.show()
