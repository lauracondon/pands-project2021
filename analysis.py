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

with open('summary.txt','w') as outfile: # need to look into formatting output
    all_class_min.to_string(outfile)
    all_class_max.to_string(outfile)
    all_class_median.to_string(outfile)
    all_class_unique.to_string(outfile)
    all_class_mean.to_string(outfile)
    all_class_std.to_string(outfile)
    all_class_mad.to_string(outfile)



set_1 = iris[iris["class"] == "Iris-setosa"]
set_2 = iris[iris["class"] == "Iris-versicolor"]
set_3 = iris[iris["class"] == "Iris-virginica"]

# scatter plot of each class individually - sepal length by sepal width 

fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharex=True, sharey=True)

ax1.plot(set_1["sepal length"], set_1["sepal width"], 'o', color = '#006ba4', label='setosa')
ax2.plot(set_2["sepal length"], set_2["sepal width"], 'o',  color = '#ff800e', label='versicolor')
ax3.plot(set_3["sepal length"], set_3["sepal width"], 'o',  color = '#595959', label='virginica')

ax1.set_title("iris-setosa")
ax2.set_title("iris-versicolor")
ax3.set_title("iris-virginica")
plt.suptitle("sepal length x sepal width")
fig.tight_layout()

plt.show()

# scatter plot of each class individually - petal length by petal width 

fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharex = True, sharey = True)

ax1.plot(set_1["petal length"], set_1["petal width"], 'o', color = '#006ba4', label='setosa')
ax2.plot(set_2["petal length"], set_2["petal width"], 'o',  color = '#ff800e', label='versicolor')
ax3.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label='virginica')

ax1.set_title("iris-setosa")
ax2.set_title("iris-versicolor")
ax3.set_title("iris-virginica")
plt.suptitle("petal length x petal width")
fig.tight_layout()

plt.show()

# scatter plot of all three together - sepal length by sepal width 

plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
plt.grid()

plt.plot(set_1["sepal length"], set_1["sepal width"], 'o', color = '#006ba4', label='setosa')
plt.plot(set_2["sepal length"], set_2["sepal width"], 'o',  color = '#ff800e', label='versicolor')
plt.plot(set_3["sepal length"], set_3["sepal width"], 'o',  color = '#595959', label='virginica')

plt.rcParams['font.family'] = 'Courier New'
 
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('')

plt.legend()
plt.show()

# scatter plot of all three together - petal length by petal width 

plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
plt.grid()

plt.plot(set_1["petal length"], set_1["petal width"], 'o', color = '#006ba4', label='setosa')
plt.plot(set_2["petal length"], set_2["petal width"], 'o',  color = '#ff800e', label='versicolor')
plt.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label='virginica')

plt.rcParams['font.family'] = 'Courier New'
 
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('')

plt.legend()
plt.show()


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



















