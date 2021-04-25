# displays and saves the following: 
# 1. summary information on the dataset to a single text file, 
# 2. histograms with kernel density estimate of each variable to png files 
# 3. scatter plot of petal and sepal pairs to png files
# 4. pairplot of the entire dataset to png file
# 5. boxplot and violinplot of the entire dataset to png files
# 6. violinplots of each variable grouped by iris class to png files
# Author: Laura Condon

#######################################################################################################################
# Modules, Libraries, Dataset
#######################################################################################################################

# import modules and libraries needed
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# import the data set and assign names to each column in it 
iris = pd.read_csv("iris.data", names = ["sepal length", "sepal width", "petal length", "petal width", "class"]) 

###################################################################################################################################
# Set Style of Plots
####################################################################################################################################

# sets the font style to use for all plots
plt.rcParams["font.family"] = "DejaVu Sans"

# creates color palette for use with sns plots
colors = ["#595959", "#5f9ed1", "#ff800e"]
sns.set_palette(sns.color_palette(colors))

# sets background grid style for all plots
sns.set_style("dark")

###########################################################################################################################
# 1. Summary Information on the Dataset
###########################################################################################################################

# prints summary statistics of the entire dataset - count, mean, std, min, quartiles, max
print("Summary Statistics of Iris Dataset\n")
describe = iris.describe()
print(describe) 

# the following sections of code all perform different calculations on the dataset
# the dataset is divided/grouped based off the three classes it contains
# then different calculations are performed on each variable
# a new DataFrame containing the resulting calculation is created and outputted to the user 

# this segment displays the lowest value of each class of variable 
print("\nLowest Value")
all_class_min = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].min()
print(all_class_min)

print("\nHighest Value")
all_class_max = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].max()
print(all_class_max)

# finding the range is useful as it helps measure variability in the dataset
print("\nRange of Values") 
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

# standard deviation is another way of showing variability in the dataset
print("\nStandard Deviation") 
all_class_std = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].std() 
print(all_class_std) 

print("\nMean Absolute Deviation") 
all_class_mad = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mad() 
print(all_class_mad) 

# saves the above dataframes to a text file 
tfile = open('summary.txt', 'w')
tfile.write("\n")
tfile.write("The Fisher Iris data set is a multivariate data set consisting of a total of one hundred \nand fifty samples of iris flowers. ")
tfile.write("Fifty samples were collected from each of three \ndifferent species of iris (iris setosa, iris virginica and iris versicolor) by Edgar Anderson. ")
tfile.write("\nFour attributes are recorded for each sample - sepal length, sepal width, petal length, \npetal width - as well as the class idenitifier (the species of iris). ")
tfile.write("All measurements are \ngiven in centimeters. ")
tfile.write("\n\nThis text file includes various numerical summaries of the variables in the dataset so \nthat the user can get a sense of the similarities and differences between the three species of iris. ")
tfile.write("\n\nOverview of All Variables:\n")
tfile.write("\n")
tfile.write(describe.to_string())
tfile.write("\n\n\n")
tfile.write("Lowest Value:\n")
tfile.write("\n")
tfile.write(all_class_min.to_string())
tfile.write("\n\n")
tfile.write("Highest Value:\n")
tfile.write("\n")
tfile.write(all_class_max.to_string())
tfile.write("\n\n")
tfile.write("Range of Values:\n")
tfile.write("\n")
tfile.write(all_class_range.to_string())
tfile.write("\n\n")
tfile.write("Median Value:\n")
tfile.write("\n")
tfile.write(all_class_median.to_string())
tfile.write("\n\n")
tfile.write("Number of Unique Values:\n")
tfile.write("\n")
tfile.write(all_class_unique.to_string())
tfile.write("\n\n")
tfile.write("Mean:\n")
tfile.write("\n")
tfile.write(all_class_mean.to_string())
tfile.write("\n\n")
tfile.write("Standard Deviation:\n")
tfile.write("\n")
tfile.write(all_class_std.to_string())
tfile.write("\n\n")
tfile.write("Mean Absolute Deviation:\n")
tfile.write("\n")
tfile.write(all_class_mad.to_string())
tfile.write("\n\n")
tfile.close()

####################################################################################################################################
# 2. Histograms with Kernel Density Estimate
####################################################################################################################################

# adds a grid behind the histogram and specifies the style of it
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
# creates a histogram plot of the sepal length from the iris dataset 
ax = sns.histplot(data = iris, x = "sepal length", 
                         hue = "class", # assigns a colour to each class based on earlier sns palette
                         kde = True, # adds a kernel density estimate overlay
                         bins = 25, # specifies how many bars to display in the histogram
                         element = "step") # specifies style of histogram bars

# adds a title in bold font
plt.title("Sepal Length Histogram with Kernel Density Estimate", weight = "bold")
# saves the resulting plot as a png file to designated subfolder 
plt.savefig("data-visualizations/histogram - sepal length with density.png") 
# displays the resulting plot in a pop up window to the user
plt.show()

# the same process is repeated for each variable in the dataset 

# histogram of sepal width
plt.rc("grid", linestyle="dotted", color="gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "sepal width", hue = "class", kde = True, bins = 25, element = "step") 
plt.title("Sepal Width Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - sepal width with density.png") 
plt.show()

# histogram of petal length
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "petal length", hue = "class", kde = True, bins = 25, element = "step") 
plt.title("Petal Length Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - petal length with density.png") 
plt.show()

# histogram of petal width
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "petal width", hue = "class", kde = True, bins = 25, element = "step") 
plt.title("Petal Width Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - petal width with density.png") 
plt.show()

####################################################################################################################################
# 3. Scatter Plots
####################################################################################################################################

set_1 = iris[iris["class"] == "Iris-setosa"]
set_2 = iris[iris["class"] == "Iris-versicolor"]
set_3 = iris[iris["class"] == "Iris-virginica"]

# scatter plot of sepal width versus length

plt.rc("grid", linestyle="dotted", color="gray", alpha=0.7)
plt.grid()

plt.plot(set_1["sepal length"], set_1["sepal width"], "o", color = "#595959", label = "setosa")
plt.plot(set_2["sepal length"], set_2["sepal width"], "o",  color = "#5f9ed1", label = "versicolor")
plt.plot(set_3["sepal length"], set_3["sepal width"], "o",  color = "#ff800e" , label = "virginica")
 
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.title("Scatterplot of Sepal Width vs. Sepal Length", weight = "bold")

plt.legend()
plt.savefig("data-visualizations/scatterplot - sepal width v length.png") 
plt.show()

# scatter plot of petal width versus petal length

plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()

plt.plot(set_1["petal length"], set_1["petal width"], "o", color = "#595959", label = "setosa")
plt.plot(set_2["petal length"], set_2["petal width"], "o",  color = "#5f9ed1", label = "versicolor")
plt.plot(set_3["petal length"], set_3["petal width"], 'o',  color = "#ff800e", label = "virginica")

plt.xlabel("petal length")
plt.ylabel("petal width")
plt.title("Scatterplot of Petal Width vs. Petal Length", weight = "bold")

plt.legend()
plt.savefig("data-visualizations/scatterplot - petal width v length.png")
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
sns.boxplot(data = iris, palette = "colorblind")
plt.title("Boxplot of Iris Variables", weight = "bold")
plt.savefig("data-visualizations/boxplot - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(data = iris, palette = "colorblind")
plt.title("Violinplot of Iris Variables", weight = "bold")
plt.savefig("data-visualizations/violinplot - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "sepal length", data = iris)
plt.title("Violinplot of Sepal Length by Class", weight = "bold")
plt.savefig("data-visualizations/violinplot by sepal length - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "sepal width", data=iris)
plt.title("Violinplot of Sepal Width by Class", weight = "bold")
plt.savefig("data-visualizations/violinplot by sepal width - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "petal length", data=iris)
plt.title("Violinplot of Petal Length by Class", weight = "bold")
plt.savefig("data-visualizations/violinplot by petal length - iris.png")
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
sns.violinplot(x= "class", y = "petal width", data=iris)
plt.title("Violinplot of Petal Width by Class", weight = "bold")
plt.savefig("data-visualizations/violinplot by petal width - iris.png")
plt.show()



