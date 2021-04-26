# Table of Contents

1. [Introduction](https://github.com/lauracondon/pands-project2021/blob/main/README.md#1-introduction)
2. [Summary of the Fisher Iris Data Set](https://github.com/lauracondon/pands-project2021/blob/main/README.md#2-summary-of-the-fisher-iris-data-set)
3. [How to Run analysis.py](https://github.com/lauracondon/pands-project2021/blob/main/README.md#3-how-to-run-analysispy)
4. [Code Explanation](https://github.com/lauracondon/pands-project2021/blob/main/README.md#4-code-explanation)
5. [Dataset Analysis](https://github.com/lauracondon/pands-project2021/blob/main/README.md#5-dataset-analysis)
6. [Why Use Python?](https://github.com/lauracondon/pands-project2021/blob/main/README.md#6-why-use-python)
7. [References](https://github.com/lauracondon/pands-project2021/blob/main/README.md#7-references)

# 1. Introduction

This github repository contains my final project for the 2021 Programming and Scripting module for GMIT's HDip in Science in Computing (Data Analytics).

Along with this README which will explain the project in detail, this repository contains the following: 

- data-visualizations - this folder contains all png files outputted by analysis.py.
- analysis.py - this Python file contains all the code used to analyse the iris dataset.
- iris.data - the version of the Fisher Iris dataset used for this project [1]. 
- summary.txt - this text file contains various numerical summaries of the variables in the     iris dataset as outputted by analysis.py. 

# 2. Summary of the Fisher Iris Data Set

The Fisher Iris data set is a multivariate data set consisting of a total of one hundred and fifty samples of iris flowers. Fifty samples were collected from each of three different species of iris (iris setosa, iris virginica and iris versicolor) by Edgar Anderson. Four attributes are recorded for each sample - sepal length, sepal width, petal length, petal width - as well as the class identifier (the species of the iris). All measurements are given in centimeters [1]. 

R.A. Fisher first published this dataset in the article 'The Use of Multiple Measurements in Taxonomic Problems' in 1936. In it, Fisher uses the dataset to create a linear discriminant model in order to classify the three different species of iris. Anderson also published an article in 1936, entitled 'The Species Problem in Iris' in which he uses the information from the dataset, in combination with additional research, to hypothesize that iris versicolor is an amphidiploid hybrid of iris setosa and iris virginica [2]. This hypothesis was confirmed by Yoong Lim et. al in 2007 in the article 'Parental Origin and Genome Evolution in the Allopolyploid Iris versicolor' [3]. 

Since its publication, Fisher's iris dataset has become tremendously popular for use in machine learning and statistics. According to Wiley Online Library, it has been cited in other publications 8,336 times - 547 times in 2020 alone, reflecting its continued popularity [5]. Wiley also records that it has been referenced in 41 patents, ranging from medical devices to a data mining and analytics suite called KnowledgeSTUDIO first released in 1999 and still available today [6]. 

Use of this dataset is not without issue, however, and there are errors that were incorporated into its reproduced versions which went unnoticed for many years. Notably, the version uploaded to the University of California at Irvine's machine learning repository contains two errors, as first noted by Besdek et. al [7]. These errors are now acknowledged by the UCI on their website [8]. Additionally some biologists have argued that iris flowers don't actually have sepals at all and instead have tepals [9]. That argument is best left to them but it is an interesting aside to a near ubiquitous dataset. 

# 3. How to Run analysis.py

If you would like to run analysis.py on your own Windows machine, you will need to have the following installed: 

1. [Anaconda](https://www.anaconda.com/products/individual) - a Python distribution platform that comes preinstalled with the basic libaries you need for data science and machine learning. 
2. [Visual Studio Code](https://code.visualstudio.com/)- a desktop code editor 

To run simply:
1. Clone the repository to your machine by following the steps in Gitgub's [guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). Note that you will also need to download [Git Bash](https://git-scm.com/downloads).

    **OR**

    download the repository as a zip file by clicking the green 'Code' button.  

2. Open the resulting folder in Visual Studio Code.
3. Navigate to analysis.py within the folder and click run. 

Alternatively you can also run Python directly from the Windows Command Line, and skip downloading Visual Studio Code, by navigating to the folder where you saved the repository and entering python analysis.py. 

# 4. Code Explanation

In this section, you’ll find a step by step breakdown of the code used in analysis.py.

Jump to:
[Step 1 - Import Required Libraries and the Iris Dataset](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-1---import-required-libraries-and-the-iris-dataset)
[Step 2 - Set Default Style](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-2---set-default-style)
[Step 3 - Summarise the Dataset](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-3---summarise-the-dataset)
[Step 4 - Histogram with Kernel Density Estimate](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-4---histogram-with-kernel-density-estimate)
[Step 5 - Scatterplots](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-5---scatterplots)
[Step 6 - Pairplot](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-6---pairplot)
[Step 7 - Boxplot and Violinplot](https://github.com/lauracondon/pands-project2021/blob/main/README.md#step-7---boxplot-and-violinplot)

### **Step 1 - Import Required Libraries and the Iris Dataset**

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
Python comes with a range of ready to use inbuilt commands but it also allows for the importation of libraries in order to increase its capabilities. The following modules and libraries are used in analysis.py:

- [pandas](https://pandas.pydata.org/) - a Python library used for data analysis and manipulation. It prides itself on being "fast, powerful, flexible and easy to use" [1]. In analysis.py pandas is used to import the iris dataset and to create the numeric summaries outputted to summary.txt. 
- [Matplotlib](https://matplotlib.org/) - a Python library used to create data visualizations. According to its slogan it "makes easy things easy and hard things possible" [2]. In analysis.py matplotlib is used to create and save scatterplots and is used to perform various actions on seaborn plots including adding titles and saving to png. 
- [seaborn](https://seaborn.pydata.org/index.html) - a Python library used to create data visualizations. It is based on Matploblib but its more streamlined approach allows you to "focus on what the different elements of your plots mean, rather than on the details of how to draw them" [3]. In analysis.py it is used to create histograms, boxplots, violinplots and to plot pairs of variables using pairplot.

```
iris = pd.read_csv("iris.data", names = ["sepal length", "sepal width", "petal length", "petal width", "class"]) 
```
Fisher's Iris dataset is read into the analysis.py as a DataFrame, so that various subdivisions, calculations and data visualizations can be performed on it [4]. Using 'names =', names are assigned to each of the five columns in the dataset in order to make them easy to work with in the code [5].


### **Step 2 - Set Default Style**

```
colors = ["#595959", "#5f9ed1", "#ff800e"]
sns.set_palette(sns.color_palette(colors))
sns.set_style("dark")
```

Here different style attributes are assigned to the graphs to be created. A custom colour palette is created for the seaborn graphs [6]. The colours chosen are taken from tableau's color blind 10 palette [7]. 

Seaborn also comes with numerous inbuilt colour palettes including pastel, dark and their own variation on colorblind which can be assigned using set_palette [8]. 

Set style is used here to add a dark background to all graphs in order to provide increased contrast with the markers, histograms etc [9]. Other preconfigured options include white, whitegrid, darkgrid and ticks.


### **Step 3 - Summarise the Dataset**

```
describe = iris.describe()
```
Pandas comes with a number of handy commands that can perform complex calculations on datasets with ease. Here '.describe()' is used to perform summary calculations on all numeric variables [10]. 
```
all_class_mean = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].mean() 
print(all_class_mean)
```
By grouping the variables, calculations can be performed on each class [11]. In this case, the mean value of each attribute for each species of iris is returned. This is a good way to get a sense of what the key differences between them are. 

There are a wide range of common calculations used in data analysis [12] that can be easily perfomed using this method as demonstrated in analysis.py [13]. 

```
tfile = open('summary.txt', 'w')
tfile.write("\n")
[...]
tfile.write("\n\nOverview of All Variables:\n")
tfile.write("\n")
tfile.write(describe.to_string())
```
In order to save the calculations so they can be easily viewed later, they are outputted to a designated text file using write. The various calculations performed above, all create a new DataFrame containing the result. As they are a DataFrame they must be converted to a string using 'to.string()' before they can be written to a text file [14]. New line ('\n') is used to improve the readability of the outputted text file.

The file is opened in write mode, rather than append, so that each time the program is run the text file is overwritten [15]. This is helpful as if you were to edit the dataset by for example adding new rows, the summary data file would change accordingly when analysis.py is next run. 


### **Step 4 - Histogram with Kernel Density Estimate**

```
plt.rc("grid", linestyle="dotted", color="gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "sepal width", hue = "class", kde = True, bins = 25, element = "step") 
plt.title("Sepal Width Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - sepal width with density.png") 
plt.show()
```

Using seaborn, histograms for each of the four numeric variables are created [16]. Histograms are a common way to visualize distributions in data. 

These histograms are multivariate as each of the three classes of iris are represented on the same graph. Using ' hue = "class"' each class is assigned a different colour - taken from the colour palette applied earlier [17]. 

A kernel density estimate (KDE) is added overlapping the histogram. A KDE is a smooth curve estimate of the density of a variable [18]. Seaborn provides an easy way to combine the two in one figure by simply including 'kde = True'. As there is quite a bit of overlap in some of the figures, efforts have been made to make the data easier to read by increasing the number of bins in the histogram and by setting the element to step so that bars overlap as one 'block' with decreased opacity [19]. Gridlines are also added to try to increase the readibility. 

The resulting histograms are both displayed to the user one at a time in a pop up window and saved to the designated folder 'data-visualizations' for later viewing [20]. As with the summary text file, if the data was changed in the iris.data file the next time analysis.py was run the figures would be overwritten with the new output.


### **Step 5 - Scatterplots**

```
set_1 = iris[iris["class"] == "Iris-setosa"]
set_2 = iris[iris["class"] == "Iris-versicolor"]
set_3 = iris[iris["class"] == "Iris-virginica"]
```
Scatterplots are used to visualize the relationship between two variables thus allowing us to determine if there are correlations between them [21]. In a scatterplot, each value in the dataset is represented by a marker. Before creating scatterplots, the dataset is divided into subsets (set_1, set_2, set_3) according to each class of iris [22].

``` 
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
```
The plt.plot function from matplotlib is used to create the scatterplots [23]. Each set or class to be included in the plot is listed individually. Different styles can then be applied to each. There are many different marker styles that can be used with matplotlib including diamonds, triangles and stars [24] Here point "." is used for all markers as its smaller size mean they overlap less. The colour is specified for each, in line with the colours used in the seaborn palette. 

Matplotlib also comes with an inbuilt function plt.scatter to create scatterplots with. This function allows the properties of each individual point (size, face colour, edge colour etc.) to be specified. For small datasets like Fisher's iris dataset there is not much difference in the efficiency of each function, but for large datasets, plt.plot can be noticeably more efficient and is this preferable [25].

These scatterplots are plotted entirely with matplotlib. While seaborn will automatically generate axes labels and a legend based off the input, in matplotlib their presence has to be specified. While this increases the amount of code required, the upside is that it makes these attributes easily editable, removable and understandable.


### **Step 6 - Pairplot**


```
sns.pairplot(iris, hue = "class", markers = [".", ".", "."], plot_kws = {"alpha": 0.6, "s": 80, "edgecolor": "k"}, height = 2) 
plt.savefig("data-visualizations/pairplot.png")
plt.show()
```
Pairplot is an excellent way to easily generate a variety of plots from a dataset. Here pairplot is used to generate a figure containing scatter plots of every combo of the iris dataset's variables and a KDE for each individual variable.

All that needs to be included to use the pairplot function is the name of the dataset and, if you wish to have different colours for each categorical variable, a hue specifier [26]. With just one line, a complex set of plots can be greated. 

Here additional code is included to specify the output's style, both in order to improve readability and to ensure consistency with the other plots. Using markers [27] and plot_kws the style of the marker for the scatterplots is set. Alpha refers to their transparency, 's' to size and 'edgecolour: k' adds a black outline to each marker [28]. The height of the plots is also specified. 

As there are a lot of plots within the same figure, the output is more compressed as a result. There are also many different axes sizes contained within the same figure, which can make it harder to read at a glance. Additionally, pairplot will take longer to run than other plotting functions. This is not a issue for the current dataset but could present problems when working with larger sets. In order to lessen this, fewer rows from the dataset could be included to give more of a snapshot overview or to only plot a certain range of the data for instance certain years [29].

Nonetheless pairplot is an extremely handy tool to generate multiple subplots easily and can provide a good indication of what more indepth forms of analysis may be worth doing on the dataset [30]. In addition to scatterplots and KDE, pairplot can be used to output univariate and bivariate histograms in different styles [31]. 

### **Step 7 - Boxplot and Violinplot**

Box plots and violin plots are both used to show the distribution of quantitative data. Boxplots show the minimum, first quartile, median, third quartile, and maximum [32] as indicated in the below figure: 

Violin plots are hybrids of a box plot and a kernel density plot [33] and are read as follows: 

```
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.boxplot(data = iris, palette = "colorblind")
plt.title("Boxplot of Iris Variables", weight = "bold")
plt.savefig("data-visualizations/boxplot - iris.png")
plt.show()
```

As with pairplot, boxplot is easy to use. Here we are generating an overall box plot of each variable and not subdividing by class. An inbuilt sns palette, colorblind, is used to visually distinguish it from the other graphs which do feature division by class [34]. A violin plot of the same is also created. Comparing the two handily shows the differences between the two types of plot. 


```
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.violinplot(x = "class", y = "sepal length", data = iris)
plt.title("Violinplot of Sepal Length by Class", weight = "bold")
plt.savefig("data-visualizations/violinplot by sepal length - iris.png")
plt.show()
```

Following this, individual violin plots of each numeric variable divided by class are created [35]. It is easy to see from them where the key differences in the iris dataset lie and that is the real strength of this type of plot. 

# 5. Dataset Analysis

What conclusions can be drawn from the dataset based off the output of analysis.py? 

Looking first at summary.txt, the following stands out: 

- The petals of iris setosa are notably shorter. Its petal length has a lowest value of 1.0 and a highest value of 1.9. Its petal width has a lowest value of 0.1 and a highest value of 0.6.  

- The petals of iris setosa also show the least amount of variance. They have a low number of unique values and the standard deviation in petal length and width is low. 

- There is little obvious difference between the sepals of each species. 

Summary statistics on their own can be deceiving, as famously demonstrated by Anscombe’s quartet [1]. When data is visualized, patterns can emerge that may otherwise have gone unnoticed. 

Looking at the histograms, scatterplots and pair plots the following can be said:
 
- Iris setosa has the smallest petals in terms of both width and length. While there is some overlap in petal length and width between iris versicolor and iris virginica, iris virginica is commonly larger. 

- While there is a lot more overlap in regards to sepal length and width, the sepals of iris setosa tend to be both shorter and wider that those of the other iris species. 

From the box plot and violin plots: 

- It’s clear that sepal width has the lowest range of values across all species. Whereas petal length has the largest range of possible values.

- Although iris setosa has the smallest range of possible values for sepal length, petal width and petal length, it has the largest range of values for sepal width.

What can we conclude: 

- Petals are overall the most useful of the dataset’s recorded attributes for determining iris species. 

- Iris setosa has the smallest petals both in terms of length and width, and wider sepals than iris versicolor and iris virginica.

- The sepal length and width of iris virginica and iris versicolor overlap a lot, so they are not useful attributes to distinguish them by. Iris virginica has the longest and widest petals of all species, so this could be used to distinguish them from the others. 

# 6. Why Use Python? 

With some many tools readibly available for data analysis and visualisation, what benefit does Python have over others?

One major plus of Python is that it is completely free to use, unlike software such as MiniTab. Python also has an active community surrounding it, meaning there are plenty of free resources and guides available online. 

Python is capable of performing complex calculations quickly and of working with datasets of all sizes. 

There is a huge variety of graphs that can be generated with Python using matplotlib and seaborn. There is also a high level of customization available. You can make your graphs as complex or as easy as you'd like them to be. Seaborn in particular requires very little code to generate complex graphs. 

It is easy to link Python to Github so you can share and backup your work online. It is also easy to save your generated graphs and text summaries in different file formats. This way they can be shared and used outside of Python. 

The data analysis demonstrated in analysis.py is just a small fraction of what Python is capable of. There are plenty of other open source libraries available, such as NumPy, Scikit-learn and StatsModels, that can be used to work with data in Python.

# 7. References 

** note - fix referencing formatting ** 

### Introduction 

[1] bezdekIris.data from the University of California at Irvine's machine learning repository. Note: this is the corrected version of the dataset and not the version with two errors. 

### Summary of the Fisher Iris Data Set

[1] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x (accessed 25/03/2021)\
[2] https://www.biodiversitylibrary.org/page/16048445#page/470/mode/1up (accessed 25/03/2021)\
[3] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735315/ (accessed 25/03/2021)\
[4] https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data (accessed 25/03/2021)\
[5] https://app.dimensions.ai/details/publication/pub.1036660865 (accessed 26/04/2021)\
[6] https://www.altair.com/knowledge-studio/ (accessed 26/04/2021)\
[7] https://lucykuncheva.co.uk/papers/jbjkrklknptfs99.pdf (accessed 25/03/2021)\
[8] https://archive.ics.uci.edu/ml/datasets/iris (accessed 25/03/2021)\
[9] https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data (accessed 25/03/2021)\

### Code Explanation

[1] https://pandas.pydata.org/ (accessed 25/04/2021)\
[2] https://matplotlib.org/ (accessed 25/04/2021)\
[3] https://seaborn.pydata.org/introduction.html (accessed 25/04/2021)\
[4] https://towardsdatascience.com/an-overview-of-importing-data-in-python-ac6aa46e0889 (accessed 08/04/2021)\
[5] https://www.kite.com/python/answers how-to-set-column-names-when-importing-a-csv-into-a-pandas-dataframe-in-python (accessed 08/04/2021)\
[6] https://towardsdatascience.com/how-to-use-your-own-color-palettes-with-seaborn-a45bf5175146(accessed 20/04/2021)\
[7] Tableau Public. *Color Palettes with RGB Values* https://public.tableau.com/profile/chris.gerrard#!/vizhome/TableauColors/ColorPaletteswithRGBValues (accessed 20/03/2021)\
[8] https://seaborn.pydata.org/tutorial/color_palettes.html (accessed 20/04/2021)\
[9] http://seaborn.pydata.org/tutorial/aesthetics.html (accessed 22/04/2021)\
[10] https://www.geeksforgeeks.org/python-pandas-dataframe-describe-method/ (accessed 23/03/2021)\
[11] Pandas for Everyone - Section 1.4 (09/04/2021)\
[12] https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_summarizingdata/bs704_summarizingdata_print.html (accessed 09/04/2021)\
[13] https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html (09/04/2021)\
[14] https://stackoverflow.com/questions/51829923/write-a-pandas-dataframe-to-a-txt-file (accessed 10/04/2021)\
[15] https://realpython.com/read-write-files-python/#reading-and-writing-opened-files (accessed 10/04/2021)\
[16] https://seaborn.pydata.org/generated/seaborn.histplot.html (accessed 13/04/2021)\
[17] https://seaborn.pydata.org/tutorial/distributions.html (accessed 13/04/2021)\
[18] Python Data Science Handbook - https://jakevdp.github.io/PythonDataScienceHandbook/05.13-kernel-density-estimation.html (accessed 16/04/2021)\
[19] https://seaborn.pydata.org/tutorial/distributions.html (accessed 13/04/2021)\
[20] https://stackoverflow.com/questions/11373610/save-matplotlib-file-to-a-directory (accessed 13/04/2021)\
[21] https://visme.co/blog/scatter-plot/ (accessed 26/04/2021)\
[22] Pandas for Everyone - Section 3.2 (09/04/2021)\
[23] Python Data Science Handbook - https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html (accessed 11/04/2021)\
[24] https://matplotlib.org/stable/api/markers_api.html (accessed 25/04/2021)\
[25] Python Data Science Handbook - https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html (accessed 11/04/2021)\
[26] https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166 (accessed 22/04/2021)\
[27] https://seaborn.pydata.org/generated/seaborn.pairplot.html (accessed 25/04/2021)\
[28] https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166 (accessed 22/04/2021)\
[29] https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166 (accessed 22/04/2021)\
[30] https://medium.com/@jaimejcheng/data-exploration-and-visualization-with-seaborn-pair-plots-40e6d3450f6d (accessed 22/04/2021)\
[31] https://seaborn.pydata.org/generated/seaborn.pairplot.html (accessed 22/04/2021)\
[32] https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/box-whisker-plots/a/box-plot-review (accessed 26/04/2021)\
[33] https://mode.com/blog/violin-plot-examples/ (accessed 26/04/2021)\
[34] https://seaborn.pydata.org/generated/seaborn.boxplot.html (accessed 13/04/2021)\
[35] https://seaborn.pydata.org/tutorial/color_palettes.html (accessed 22/04/2021)
[36] https://seaborn.pydata.org/generated/seaborn.violinplot.html (accessed 13/04/2021)\

### Dataset Analysis

[1] Pandas for Everyone - Section 3.1/n

