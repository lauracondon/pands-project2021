# outputs a summary of each variable to a single text file, 
# saves a histogram of each variable to png files 
# outputs a scatter plot of each pair of variables
# what else should I do along with these
# Author: Laura Condon

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.data", names=["sepal length", "sepal width", "petal length", "petal width", "class"]) # names assigns column names to the dataset
# print(iris.head()) # prints the first five rows
# print(type(ir)) # checks type of the object
# print(iris.shape) # tells you how many rows and columns in set
# print(iris.columns) # prints names of columns
# print(iris.dtypes) # get the datatype of each column
# print(iris.info()) # gets information about dataset including memory usage

sepal_length = iris[["sepal length"]] # create subset based on columns
sepal_width = iris[["sepal width"]]
petal_length = iris[["petal length"]]
petal_width = iris[["petal width"]]
sepal_subset = iris[["sepal length", "sepal width"]] 
petal_subset = iris[["petal length", "petal width"]]
#print(sepal_subset)
#print(petal_subset)
#print(sepal_length)

setosa = iris.iloc[0:50] # create subset based on rows to seperate each class of iris
versicolor = iris.iloc[50:100]
virginica = iris.iloc[100:150]
#print(setosa)
#print(versicolor)
#print(virginica)

mean1 = iris["sepal length"].mean()
#print(round(mean1,2))
mean2 = iris["sepal width"].mean()
#print(round(mean2,2))

# how best to display it in text file? 
# the variables are sepal length, sepal width, petal length, petal height and class
# I plan to include the following in variable summary - 1. maximum 2. minimum 3. mode 4. median 5. mean 6. standard deviation
# for total set? and for each individual class? should I sample - set is already small..















