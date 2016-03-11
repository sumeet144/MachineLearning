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

