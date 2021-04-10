# outputs a summary of each variable to a single text file, 
# saves a histogram of each variable to png files 
# outputs a scatter plot of each pair of variables
# Author: Laura Condon

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv("iris.data", names=["sepal length", "sepal width", "petal length", "petal width", "class"]) # names assigns column names to the dataset

print(iris.describe()) # prints summary statistics of the entire dataset - count, mean, std, min, quartiles, max

print("Lowest Value")
all_class_min = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].min()
print(all_class_min)

print("\nHighest Value")
all_class_max = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].max()
print(all_class_max)

print("\nRange of Values") # range - measures variability
all_class_range = all_class_max - all_class_min 
print(all_class_range)

print("\nMedian Value")
all_class_median = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].median()
print(all_class_median) 

print("\nNumber of Unique Values")
all_class_unique = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].nunique()
print(all_class_unique)

print("\nMean")
all_class_mean = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mean() 
print(all_class_mean)

print("\nStandard Deviation") # standard deviation - measure variability 
all_class_std = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].std() 
print(all_class_std) 

print("\nMean Absolute Deviation") 
all_class_mad = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mad() 
print(all_class_mad) 

# mode - most frequent value
#all_class_mode = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].agg(pd.Series.mode)
#print(all_class_mode) # this doesn't work

with open('summary.txt','w') as outfile: # need to look into formatting output better
    all_class_min.to_string(outfile)
    all_class_max.to_string(outfile)
    all_class_median.to_string(outfile)
    all_class_unique.to_string(outfile)
    all_class_mean.to_string(outfile)
    all_class_std.to_string(outfile)
    all_class_mad.to_string(outfile)



# different subsets of the dataset
# sepal_length = iris[["sepal length"]] # create subset based on columns
# sepal_width = iris[["sepal width"]]
# petal_length = iris[["petal length"]]
# petal_width = iris[["petal width"]]
# sepal_subset = iris[["sepal length", "sepal width"]] 
# petal_subset = iris[["petal length", "petal width"]]
# setosa = iris.iloc[0:50] # create subset based on rows to seperate each class of iris
# versicolor = iris.iloc[50:100]
# virginica = iris.iloc[100:150]

# print(sepal_length.describe())
# print(sepal_width.describe())
# print(petal_length.describe())
# print(petal_width.describe())























