# outputs a summary of each variable to a single text file, 
# saves a histogram of each variable to png files 
# outputs a scatter plot of each pair of variables
# Author: Laura Condon

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("iris.data", names=["sepal length", "sepal width", "petal length", "petal width", "class"]) # names assigns column names to the dataset

print(iris.describe()) # prints summary statistics of the entire dataset - count, mean, std, min, quartiles, max

# print("Lowest Value")
# all_class_min = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].min()
# print(all_class_min)

# print("Highest Value")
# all_class_max = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].max()
# print(all_class_max)

# print("Range of Values") # range - measures variability
# all_class_range = all_class_max - all_class_min 
# print(all_class_range)

# print("Median Value")
# all_class_median = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].median()
# print(all_class_median) 

# print("Number of Unique Values")
# all_class_unique = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].nunique()
# print(all_class_unique)

# print("Mean")
# all_class_mean = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mean() 
# print(all_class_mean)

# print("Standard Deviation") # standard deviation - measure variability 
# all_class_std = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].std() 
# print(all_class_std) 

# print("Mean Absolute Deviation") 
# all_class_mad = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mad() 
# print(all_class_mad) 

# with open('summary.txt','w') as outfile: # need to look into formatting output
#     all_class_min.to_string(outfile) 
#     all_class_max.to_string(outfile)
#     all_class_median.to_string(outfile)
#     all_class_unique.to_string(outfile)
#     all_class_mean.to_string(outfile)
#     all_class_std.to_string(outfile)
#     all_class_mad.to_string(outfile)

plt.rcParams['font.family'] = "DejaVu Sans"

set_1 = iris[iris["class"] == "Iris-setosa"]
set_2 = iris[iris["class"] == "Iris-versicolor"]
set_3 = iris[iris["class"] == "Iris-virginica"]


# basic histogram - might remove later and just keep density plots
# set_1.hist(bins=5)
# plt.show()
# set_2.hist(bins=5)
# plt.show()
# set_3.hist(bins=5)
# plt.show()
# iris.hist(bins=10)
# plt.show()

# # scatter plot of each class individually - sepal length by sepal width 

# fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharex=True, sharey=True)

# ax1.plot(set_1["sepal length"], set_1["sepal width"], 'o', color = '#006ba4', label='setosa')
# ax2.plot(set_2["sepal length"], set_2["sepal width"], 'o',  color = '#ff800e', label='versicolor')
# ax3.plot(set_3["sepal length"], set_3["sepal width"], 'o',  color = '#595959', label='virginica')


# ax1.set_title("iris-setosa")
# ax2.set_title("iris-versicolor")
# ax3.set_title("iris-virginica")
# ax1.grid(linestyle='dotted', color='gray', alpha=0.7)
# ax2.grid(linestyle='dotted', color='gray', alpha=0.7)
# ax3.grid(linestyle='dotted', color='gray', alpha=0.7)
# plt.suptitle("sepal length x sepal width")

# fig.text(0.5,0.009, "sepal length", ha="center", va="center", weight="bold")
# fig.text(0.015,0.5, "sepal width", ha="center", va="center", rotation=90, weight="bold")

# fig.tight_layout()

# plt.savefig("data-visualizations/subplots - sepal length by width.png")

# plt.show()

# # scatter plot of each class individually - petal length by petal width 

# fig, (ax1, ax2, ax3) = plt.subplots(1,3, sharex = True, sharey = True)

# ax1.plot(set_1["petal length"], set_1["petal width"], 'o', color = '#006ba4', label='setosa')
# ax2.plot(set_2["petal length"], set_2["petal width"], 'o',  color = '#ff800e', label='versicolor')
# ax3.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label='virginica')

# ax1.set_title("iris-setosa")
# ax2.set_title("iris-versicolor")
# ax3.set_title("iris-virginica")
# ax1.grid(linestyle='dotted', color='gray', alpha=0.7)
# ax2.grid(linestyle='dotted', color='gray', alpha=0.7)
# ax3.grid(linestyle='dotted', color='gray', alpha=0.7)
# plt.suptitle("petal length x petal width")

# fig.text(0.5,0.009, "sepal length", ha="center", va="center", weight="bold")
# fig.text(0.015,0.5, "sepal width", ha="center", va="center", rotation=90, weight="bold")

# fig.tight_layout()

# plt.savefig("data-visualizations/subplots - petal length by width.png") 

# plt.show()

# scatter plot of all three together - sepal length by sepal width 

# plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
# plt.grid()

# plt.plot(set_1["sepal length"], set_1["sepal width"], 'o', color = '#006ba4', label='setosa')
# plt.plot(set_2["sepal length"], set_2["sepal width"], 'o',  color = '#ff800e', label='versicolor')
# plt.plot(set_3["sepal length"], set_3["sepal width"], 'o',  color = '#595959', label='virginica')
 
# plt.xlabel('sepal length')
# plt.ylabel('sepal width')
# plt.title('')

# plt.legend()
# plt.savefig("data-visualizations/scatterplot - sepal length by width.png") 
# plt.show()

# scatter plot of all three together - petal length by petal width 

# plt.rc('grid', linestyle='dotted', color='gray', alpha=0.7)
# plt.grid()

# plt.plot(set_1["petal length"], set_1["petal width"], 'o', color = '#006ba4', label='setosa')
# plt.plot(set_2["petal length"], set_2["petal width"], 'o',  color = '#ff800e', label='versicolor')
# plt.plot(set_3["petal length"], set_3["petal width"], 'o',  color = '#595959', label='virginica')
 
# plt.xlabel('petal length')
# plt.ylabel('petal width')
# plt.title('')

# plt.legend()
# plt.savefig("data-visualizations/scatterplot - petal length by width.png")
# plt.show()

# density plots of each variable

ax = sns.displot(data = iris, x=  "petal width", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kind = "kde", fill = "true", bw_adjust=.50) 
plt.title("Petal Width Density", size = 15)
ax.fig.subplots_adjust(top=.9)
plt.savefig("data-visualizations/petal width density.png") 
plt.show()

ax = sns.displot(data = iris, x=  "petal length", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kind = "kde", fill = "true", bw_adjust=.50) 
plt.title("Petal Length Density", size = 15)
ax.fig.subplots_adjust(top=.9)
plt.savefig("data-visualizations/petal length density.png") 
plt.show()

ax = sns.displot(data = iris, x=  "sepal width", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kind = "kde", fill = "true", bw_adjust=.50) 
plt.title("Sepal Width Density", size = 15)
ax.fig.subplots_adjust(top=.9)
plt.savefig("data-visualizations/sepal width density.png") 
plt.show()

ax = sns.displot(data = iris, x=  "sepal length", hue = "class", palette = ["#006ba4", "#ff800e", "#595959"], kind = "kde", fill = "true", bw_adjust=.50) 
plt.title("Sepal Length Density", size = 15)
ax.fig.subplots_adjust(top=.9)
plt.savefig("data-visualizations/sepal length density.png") 
plt.show()


# # different subsets of the dataset
# # sepal_length = iris[["sepal length"]] # create subset based on columns
# #sepal_width = iris[["sepal width"]]
# # petal_length = iris[["petal length"]]
# # petal_width = iris[["petal width"]]
# # sepal_subset = iris[["sepal length", "sepal width"]] 
# # petal_subset = iris[["petal length", "petal width"]]
# #setosa = iris.iloc[0:50] # create subset based on rows to seperate each class of iris
# # versicolor = iris.iloc[50:100]
# # virginica = iris.iloc[100:150]


















