# outputs a summary of each variable to a single text file, 
# saves a histogram with kernel density estimate of each variable to png files 
# saves a scatter plot of each pair of variables to png files
# Author: Laura Condon

# import modules and libraries needed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the data set and assign names to each column in it 
iris = pd.read_csv("iris.data", names=["sepal length", "sepal width", "petal length", "petal width", "class"]) # names assigns column names to the dataset

###################################################################################################################################
# Data Summary
###################################################################################################################################

# prints summary statistics of the entire dataset - count, mean, std, min, quartiles, max
print(iris.describe()) 

# the following segments of code all perform different calculations on the dataset
# the dataset is divided based off the three classes it contains
# then different calculations are performed on each each variable
# a new DataFrame containing the resulting calculation is created

# this segment displays the lowest value of each class of variable 
print("Lowest Value")
all_class_min = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].min()
print(all_class_min)

print("Highest Value")
all_class_max = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].max()
print(all_class_max)

# finding the range is useful as it helps measure variability in the dataset
print("Range of Values") 
all_class_range = all_class_max - all_class_min 
print(all_class_range)

print("Median Value")
all_class_median = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].median()
print(all_class_median) 

print("Number of Unique Values")
all_class_unique = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].nunique()
print(all_class_unique)

print("Mean")
all_class_mean = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mean() 
print(all_class_mean)

# standard deviation is another way of showing variability in the dataset
print("Standard Deviation") 
all_class_std = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].std() 
print(all_class_std) 

print("Mean Absolute Deviation") 
all_class_mad = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mad() 
print(all_class_mad) 

# this converts the dataframes into strings and outputs to a text file
with open('summary.txt','w') as outfile: # need to look into formatting output
    all_class_min.to_string(outfile) 
    all_class_max.to_string(outfile)
    all_class_median.to_string(outfile)
    all_class_unique.to_string(outfile)
    all_class_mean.to_string(outfile)
    all_class_std.to_string(outfile)
    all_class_mad.to_string(outfile)

####################################################################################################################################
# histograms
####################################################################################################################################

plt.rcParams['font.family'] = "DejaVu Sans"

ax = sns.histplot(data = iris, x=  "petal width", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kde = True, bins = 20) 
plt.title("Petal Width Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - petal width with density.png") 
plt.show()

ax = sns.histplot(data = iris, x=  "petal length", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kde = True, bins = 20) 
plt.title("Petal Length Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - petal length with density.png") 
plt.show()

ax = sns.histplot(data = iris, x=  "sepal width", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kde = True, bins = 20) 
plt.title("Sepal Width Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - sepal width with density.png") 
plt.show()

ax = sns.histplot(data = iris, x=  "sepal length", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kde = True, bins = 20) 
plt.title("Sepal Length Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - sepal length with density.png") 
plt.show()

####################################################################################################################################
# scatter plots
####################################################################################################################################

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
ax1.grid(linestyle='dotted', color='gray', alpha=0.7)
ax2.grid(linestyle='dotted', color='gray', alpha=0.7)
ax3.grid(linestyle='dotted', color='gray', alpha=0.7)
plt.suptitle("sepal length x sepal width")

fig.text(0.5,0.009, "sepal length", ha="center", va="center", weight="bold")
fig.text(0.015,0.5, "sepal width", ha="center", va="center", rotation=90, weight="bold")

fig.tight_layout()

plt.savefig("data-visualizations/subplots - sepal length by width.png")

plt.show()

# scatter plot of each class individually - petal length by petal width 

fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharex = True, sharey = True)

ax1.plot(set_1["petal length"], set_1["petal width"], 'o', color = '#006ba4', label='setosa')
ax2.plot(set_2["petal length"], set_2["petal width"], 'o',  color = '#ff800e', label='versicolor')
ax3.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label='virginica')

ax1.set_title("iris-setosa")
ax2.set_title("iris-versicolor")
ax3.set_title("iris-virginica")
ax1.grid(linestyle='dotted', color='gray', alpha=0.7)
ax2.grid(linestyle='dotted', color='gray', alpha=0.7)
ax3.grid(linestyle='dotted', color='gray', alpha=0.7)
plt.suptitle("petal length x petal width")

fig.text(0.5,0.009, "sepal length", ha="center", va="center", weight="bold")
fig.text(0.015,0.5, "sepal width", ha="center", va="center", rotation=90, weight="bold")

fig.tight_layout()

plt.savefig("data-visualizations/subplots - petal length by width.png") 

plt.show()

# scatter plot of all three together - sepal length by sepal width 

plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
plt.grid()

plt.plot(set_1["sepal length"], set_1["sepal width"], 'o', color = '#006ba4', label='setosa')
plt.plot(set_2["sepal length"], set_2["sepal width"], 'o',  color = '#ff800e', label='versicolor')
plt.plot(set_3["sepal length"], set_3["sepal width"], 'o',  color = '#595959', label='virginica')
 
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.title('')

plt.legend()
plt.savefig("data-visualizations/scatterplot - sepal length by width.png") 
plt.show()

# scatter plot of all three together - petal length by petal width 

plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
plt.grid()

plt.plot(set_1["petal length"], set_1["petal width"], 'o', color = '#006ba4', label='setosa')
plt.plot(set_2["petal length"], set_2["petal width"], 'o',  color = '#ff800e', label='versicolor')
plt.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label='virginica')

plt.xlabel('petal length')
plt.ylabel('petal width')
plt.title('')

plt.legend()
plt.savefig("data-visualizations/scatterplot - petal length by width.png")
plt.show()

####################################################################################################################################
# box plot and violin plots
####################################################################################################################################

sns.boxplot(data = iris)
plt.show()

sns.violinplot(data = iris)
plt.show()

sns.violinplot(x= "class", y = "sepal length", data=iris)
plt.show()

sns.violinplot(x= "class", y = "sepal width", data=iris)
plt.show()

sns.violinplot(x= "class", y = "petal length", data=iris)
plt.show()

sns.violinplot(x= "class", y = "petal width", data=iris)
plt.show()

















