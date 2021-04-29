# displays and saves the following: 
# 1. summary information on the dataset to a single text file, 
# 2. histograms with kernel density estimate of each numeric variable to png files 
# 3. scatterplots of petal and sepal pairs to png files
# 4. pairplot of the entire dataset to png file
# 5. boxplot and violinplot of the entire dataset to png files
# 6. violinplots of each numeric variable grouped by iris species to png files

# Author: Laura Condon
# Note: references are indicated by numbers in square brackets
# then listed in full at the end of the code

#######################################################################################################################
# Import Libraries & Dataset
#######################################################################################################################

# imports libraries needed
# 'as' is used to specify how to refer to them in the code
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# imports the data set and assigns names to each column in it [1]
iris = pd.read_csv("iris.data", names = ["sepal length", "sepal width", "petal length", "petal width", "species"]) 

#########################################################################################################################
# Set Style of Plots
#########################################################################################################################

# creates default color palette for use with sns plots [2]
colors = ["#595959", "#5f9ed1", "#ff800e"]
sns.set_palette(sns.color_palette(colors))

# sets background of all graphs to dark [3]
sns.set_style("dark")

#########################################################################################################################
# 1. Summary Information on the Dataset
#########################################################################################################################

# prints summary statistics of the entire dataset - count, mean, std, min, quartiles, max [4]
print("Summary Statistics of Iris Dataset\n")
describe = iris.describe()
print(describe) 

# the following sections of code all perform different calculations on the dataset
# the dataset is divided/grouped based off the three species it contains [5]
# then different calculations are performed on each variable [6]
# a new DataFrame containing the resulting calculation is created and outputted to the user 

print("\nLowest Value")
all_species_min = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].min()
print(all_species_min)

print("\nHighest Value")
all_species_max = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].max()
print(all_species_max)

# finding the range is useful as it helps measure variability in the dataset
print("\nRange of Values") 
all_species_range = all_species_max - all_species_min 
print(all_species_range)

print("\nMedian Value")
all_species_median = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].median()
print(all_species_median) 

print("\nNumber of Unique Values")
all_species_unique = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].nunique()
print(all_species_unique)

print("\nMean")
all_species_mean = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].mean() 
print(all_species_mean)

# standard deviation is another way of showing variability in the dataset
print("\nStandard Deviation") 
all_species_std = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].std() 
print(all_species_std) 

print("\nMean Absolute Deviation") 
all_species_mad = iris.groupby(["species"])[["sepal length","sepal width","petal length", "petal width"]].mad() 
print(all_species_mad) 

# saves the above dataframes to a text file with added introduction [7][8]
tfile = open("summary.txt", "w")
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
tfile.write(all_species_min.to_string())
tfile.write("\n\n")
tfile.write("Highest Value:\n")
tfile.write("\n")
tfile.write(all_species_max.to_string())
tfile.write("\n\n")
tfile.write("Range of Values:\n")
tfile.write("\n")
tfile.write(all_species_range.to_string())
tfile.write("\n\n")
tfile.write("Median Value:\n")
tfile.write("\n")
tfile.write(all_species_median.to_string())
tfile.write("\n\n")
tfile.write("Number of Unique Values:\n")
tfile.write("\n")
tfile.write(all_species_unique.to_string())
tfile.write("\n\n")
tfile.write("Mean:\n")
tfile.write("\n")
tfile.write(all_species_mean.to_string())
tfile.write("\n\n")
tfile.write("Standard Deviation:\n")
tfile.write("\n")
tfile.write(all_species_std.to_string())
tfile.write("\n\n")
tfile.write("Mean Absolute Deviation:\n")
tfile.write("\n")
tfile.write(all_species_mad.to_string())
tfile.write("\n\n")
tfile.close()

##########################################################################################################################
# 2. Histograms with Kernel Density Estimate
##########################################################################################################################

# adds background grid and specifies its linestyle
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
# creates a histogram plot of the sepal length from the iris dataset [9]
ax = sns.histplot(data = iris, x = "sepal length", 
                         hue = "species", # assigns a colour to each species based on earlier sns palette
                         kde = True, # adds a kernel density estimate overlay [10]
                         bins = 25, # specifies how many bars to display in the histogram
                         element = "step") # specifies style of histogram bars

# adds a title in bold font
plt.title("Sepal Length Histogram with Kernel Density Estimate", weight = "bold")
# saves the resulting plot as a png file to designated subfolder [11]
plt.savefig("data-visualizations/histogram - sepal length with density.png") 
# displays the resulting plot in a pop up window to the user
plt.show()

# the same process is repeated for each numeric variable in the dataset 

# histogram of sepal width
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "sepal width", hue = "species", kde = True, bins = 25, element = "step") 
plt.title("Sepal Width Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - sepal width with density.png") 
plt.show()

# histogram of petal length
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "petal length", hue = "species", kde = True, bins = 25, element = "step") 
plt.title("Petal Length Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - petal length with density.png") 
plt.show()

# histogram of petal width
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "petal width", hue = "species", kde = True, bins = 25, element = "step") 
plt.title("Petal Width Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - petal width with density.png") 
plt.show()

#########################################################################################################################
# 3. Scatter Plots
#########################################################################################################################

# divides the dataset into three 'sets' based off the species of iris [12]
set_1 = iris[iris["species"] == "Iris-setosa"]
set_2 = iris[iris["species"] == "Iris-versicolor"]
set_3 = iris[iris["species"] == "Iris-virginica"]

# adds background grid and specifies its linestyle
plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
# using the sets, plots the sepal width vs. length for each species [13]
plt.plot(set_1["sepal length"], set_1["sepal width"], 
                                            ".", # sets marker style as a small circle [14]
                                            color = "#595959", # sets marker colour
                                            label = "setosa") # associate species name with marker
# the process is repeated for each set
plt.plot(set_2["sepal length"], set_2["sepal width"], ".",  color = "#5f9ed1", label = "versicolor")
plt.plot(set_3["sepal length"], set_3["sepal width"], ".",  color = "#ff800e" , label = "virginica")
# adds relevant label to x and y axis
plt.xlabel("sepal length")
plt.ylabel("sepal width")
# adds bold title to graph
plt.title("Scatterplot of Sepal Width vs. Sepal Length", weight = "bold")
# displays a legend - names are taken from label above
plt.legend()
# saves resulting plot to designated subfolder
plt.savefig("data-visualizations/scatterplot - sepal width v length.png") 
# displays plot to user in pop up window
plt.show()

# the process is repeated for a scatter plot of the petal width vs. length
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()

plt.plot(set_1["petal length"], set_1["petal width"], ".", color = "#595959", label = "setosa")
plt.plot(set_2["petal length"], set_2["petal width"], ".",  color = "#5f9ed1", label = "versicolor")
plt.plot(set_3["petal length"], set_3["petal width"], ".",  color = "#ff800e", label = "virginica")

plt.xlabel("petal length")
plt.ylabel("petal width")
plt.title("Scatterplot of Petal Width vs. Petal Length", weight = "bold")

plt.legend()
plt.savefig("data-visualizations/scatterplot - petal width v length.png")
plt.show()

###########################################################################################################################
# 4. Pairplot
###########################################################################################################################

# creates scatter plots of different combinations of the iris dataset's numeric variables
# and a kernel density estimate (KDE) for each individual numeric variable
# displays all as subplots in one figure [15]
sns.pairplot(iris, 
            hue = "species", # specifies colour based off species of iris
            markers = [".", ".", "."], # sets marker style as a small circle
            plot_kws = {"alpha": 0.6, "s": 80, "edgecolor": "k"}, # sets style, incl. opacity, for markers [16]
            height = 2) # sets height of each subplot
# saves the figure to specified subfolder
plt.savefig("data-visualizations/pairplot.png")
# displays figure to user in a pop up window
plt.show()

##########################################################################################################################
# 5. Boxplot and Violinplot of Entire Dataset
##########################################################################################################################

# specifies linestyle of background grid
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
# creates a boxplot based off entire iris dataset [17]
# uses inbuilt sns colour palette 'colorblind' [18]
sns.boxplot(data = iris, palette = "colorblind")
# adds bold title to boxplot
plt.title("Boxplot of Iris Variables", weight = "bold")
# saves resulting plot to designated subfolder
plt.savefig("data-visualizations/boxplot - iris.png")
# displays plot to user in pop up window
plt.show()

plt.rc("grid", linestyle = "dotted", color = "gray", alpha=0.7)
plt.grid()
# creates a violinplot based off entire iris dataset [19]
sns.violinplot(data = iris, palette = "colorblind")
plt.title("Violinplot of Iris Variables", weight = "bold")
plt.savefig("data-visualizations/violinplot - iris.png")
plt.show()

#########################################################################################################################
# 6. Violinplots of Each Variable 
#########################################################################################################################

# the below code works the same as the above but instead of using the entire dataset,
# individual numeric variables are chosen and plotted by species
# no palette is mentioned so it uses the default set 'colors' palette

# violinplot of sepal length
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.violinplot(x = "species", y = "sepal length", data = iris)
plt.title("Violinplot of Sepal Length by Species", weight = "bold")
plt.savefig("data-visualizations/violinplot by sepal length - iris.png")
plt.show()

# violinplot of sepal width
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.violinplot(x = "species", y = "sepal width", data = iris)
plt.title("Violinplot of Sepal Width by Species", weight = "bold")
plt.savefig("data-visualizations/violinplot by sepal width - iris.png")
plt.show()

# violinplot of petal length
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.violinplot(x = "species", y = "petal length", data = iris)
plt.title("Violinplot of Petal Length by Species", weight = "bold")
plt.savefig("data-visualizations/violinplot by petal length - iris.png")
plt.show()

# violinplot of petal width
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.violinplot(x= "species", y = "petal width", data = iris)
plt.title("Violinplot of Petal Width by Species", weight = "bold")
plt.savefig("data-visualizations/violinplot by petal width - iris.png")
plt.show()

#######################################################################################################################
# References
#######################################################################################################################

# [1] https://towardsdatascience.com/an-overview-of-importing-data-in-python-ac6aa46e0889 (accessed 08/04/2021)
# [2] https://towardsdatascience.com/how-to-use-your-own-color-palettes-with-seaborn-a45bf5175146 (accessed 20/04/2021)
# [3] http://seaborn.pydata.org/tutorial/aesthetics.html (accessed 22/04/2021)
# [4] https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/ (accessed 23/03/2021)
# [5] Daniel Y. Chen. Pandas for Everyone - 1.4 Grouped and Aggregated Calculations 
# [6] https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html (09/04/2021)
# [7] https://stackoverflow.com/questions/51829923/write-a-pandas-dataframe-to-a-txt-file (accessed 10/04/2021)
# [8] https://realpython.com/read-write-files-python/#reading-and-writing-opened-files (accessed 10/04/2021)
# [9] https://seaborn.pydata.org/generated/seaborn.histplot.html (accessed 13/04/2021)
# [10] https://jakevdp.github.io/PythonDataScienceHandbook/05.13-kernel-density-estimation.html (accessed 16/04/2021)
# [11] https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory (accessed 13/04/2021)
# [12] Daniel Y. Chen. Pandas for Everyone - 3.2 Matplotlib (2018, Addison-Wesley)
# [13] https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html (accessed 11/04/2021)
# [14] https://matplotlib.org/stable/api/markers_api.html (accessed 25/04/2021)
# [15] https://seaborn.pydata.org/generated/seaborn.pairplot.html (accessed 25/04/2021)
# [16] https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166 (accessed 22/04/2021)
# [17] https://seaborn.pydata.org/generated/seaborn.boxplot.html (accessed 13/04/2021)
# [18] https://seaborn.pydata.org/tutorial/color_palettes.html (accessed 22/04/2021)
# [19] https://seaborn.pydata.org/generated/seaborn.violinplot.html (accessed 13/04/2021)
