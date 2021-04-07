# outputs a summary of each variable to a single text file, 
# saves a histogram of each variable to png files 
# outputs a scatter plot of each pair of variables
# Author: Laura Condon

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ir = pd.read_csv("iris.data", names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class']) # names assigns column names to the dataset
print(ir.head()) # prints the first five rows
print(type(ir)) # checks type of the object
print(ir.shape) # tells you how many rows and columns in set
print(ir.columns) # prints names of columns
print(ir.dtypes)
print(ir.info())