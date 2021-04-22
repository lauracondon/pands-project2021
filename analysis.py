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
iris = pd.read_csv("iris.data", names = ["sepal length", "sepal width", "petal length", "petal width", "class"]) 

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
with open("summary.txt","w") as outfile: # need to look into formatting output
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

# sets the font style to use for all the following plots

sns.set_style("dark")
plt.rcParams["font.family"] = "DejaVu Sans"
colors = ["#595959", "#5f9ed1","#ff800e","#006ba4",  ]
sns.set_palette(sns.color_palette(colors))

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()

# creates a histogram plot with a kernel density estimate of the 'petal width' from the iris dataset
# it assigns colour to each class in the dataset ('hue =') and it uses 'palette' to specify what colour
# 'kde = True' - adds a kernel density estimate overlay
# 'bins' specifies how many bars to display in the histogram
ax = sns.histplot(data = iris, x = "petal width", hue = "class", kde = True, bins = 20, element = "step") 

# adds a title and specifies font size
plt.title("Petal Width Histogram with Density", size = 15)
# saves the resulting figure to a subfolder 
plt.savefig("data-visualizations/histogram - petal width with density.png") 
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
# the same process is repeated for each variable in the dataset 
ax = sns.histplot(data = iris, x = "petal length", hue = "class", kde = True, bins = 20, element = "step") 
plt.title("Petal Length Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - petal length with density.png") 
plt.show()

plt.rc("grid", linestyle="dotted", color="gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "sepal width", hue = "class", kde = True, bins = 20, element = "step") 
plt.title("Sepal Width Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - sepal width with density.png") 
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "sepal length", hue = "class", kde = True, bins = 20, element = "step") 
plt.title("Sepal Length Histogram with Density", size = 15)
plt.savefig("data-visualizations/histogram - sepal length with density.png") 
plt.show()

####################################################################################################################################
# scatter plots
####################################################################################################################################

set_1 = iris[iris["class"] == "Iris-setosa"]
set_2 = iris[iris["class"] == "Iris-versicolor"]
set_3 = iris[iris["class"] == "Iris-virginica"]


# scatter plot of sepal length by sepal width 

plt.rc("grid", linestyle="dotted", color="gray", alpha=0.7)
plt.grid()

plt.plot(set_1["sepal length"], set_1["sepal width"], "o", color = "#006ba4", label = "setosa")
plt.plot(set_2["sepal length"], set_2["sepal width"], "o",  color = "#ff800e", label = "versicolor")
plt.plot(set_3["sepal length"], set_3["sepal width"], "o",  color = "#595959", label = "virginica")
 
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.title("Sepal Length x Sepal Width - Scatterplot")

plt.legend()
plt.savefig("data-visualizations/scatterplot - sepal length by width.png") 
plt.show()

# scatter plot of petal length by petal width 

plt.rc("grid", linestyle="dotted", color="gray", alpha=0.7)
plt.grid()

plt.plot(set_1["petal length"], set_1["petal width"], "o", color = "#006ba4", label = "setosa")
plt.plot(set_2["petal length"], set_2["petal width"], "o",  color = "#ff800e", label = "versicolor")
plt.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label = "virginica")

plt.xlabel("petal length")
plt.ylabel("petal width")
plt.title("Petal Length x Petal Width - Scatterplot")

plt.legend()
plt.savefig("data-visualizations/scatterplot - petal length by width.png")
plt.show()

########################################################################################################################
# pairplot
########################################################################################################################

sns.pairplot(iris, hue = "class", plot_kws = {"alpha": 0.6, "s": 80, "edgecolor": "k"}, height = 4)
plt.savefig("data-visualizations/pairplot.png")
plt.show()

####################################################################################################################################
# box plot and violin plots
####################################################################################################################################

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.boxplot(data = iris)
plt.savefig("data-visualizations/boxplot - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(data = iris)
plt.savefig("data-visualizations/violinplot - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "sepal length", data=iris)
plt.savefig("data-visualizations/violinplot by sepal length - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "sepal width", data=iris)
plt.savefig("data-visualizations/violinplot by sepal width - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "petal length", data=iris)
plt.savefig("data-visualizations/violinplot by petal length - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "petal width", data=iris)
plt.savefig("data-visualizations/violinplot by petal width - iris.png")
plt.show()

