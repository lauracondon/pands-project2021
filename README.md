# Table of Contents

1. Introduction
2. Summary of the Fisher Iris Data Set
3. How to Run analysis.py
4. Code Explanation
5. Dataset Analysis 
6. Why Use Python? 
7. References 

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

Since its publication, Fisher's iris dataset has become tremendously popular for use in machine learning and statistics. According to Wiley Online Library, it has been cited in other publications 7,422 times [5].  

Use of this dataset is not without issue, however, and there are errors that were incorporated into its reproduced versions which went unnoticed for many years. Notably, the version uploaded to the University of California at Irvine's machine learning repository contains two errors, as first noted by Besdek et. al [6].  These errors are now acknowledged by the UCI on their website [7]. Additionally some biologists have argued that iris flowers don't actually have sepals at all and instead have tepals [8]. That argument is best left to them but it is an interesting aside to a near ubiquitous dataset. 

# 3. How to Run analysis.py

If you would like to run analysis.py on your own Windows machine, you will need to have the following installed: 

1. [Anaconda](https://www.anaconda.com/products/individual) - a Python distribution platform that comes preinstalled with the basic libaries you need for data science and machine learning. 
2. [Visual Studio Code](https://code.visualstudio.com/)- a desktop code editor 

To run simply:
1. Clone the repository to your machine by following the steps in Gitgub's [guide](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). Note that you will also need to download [Git Bash](https://git-scm.com/downloads).

    OR 

    download the repository as a zip file by clicking the green 'Code' button.  

2. Open the resulting folder in Visual Studio Code.
3. Navigate to analysis.py within the folder and click run. 

Alternatively you can also run Python directly from the Windows Command Line, and skip downloading Visual Studio Code, by navigating to the folder where you saved the repository and entering python analysis.py. 

# 4. Code Explanation

In this section, you’ll find a step by step breakdown of the code used in analysis.py.

1. Import required libraries and the iris dataset

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
Fisher's Iris dataset is read into the analysis.py as a DataFrame, so that various subdivisions, calculations and data visualizations can be performed on it. Using 'names =', names are assigned to each of the five columns in the dataset in order to make them easy to work with in the code. 

2. Set default style 


```
plt.rcParams["font.family"] = "DejaVu Sans"
colors = ["#595959", "#5f9ed1", "#ff800e"]
sns.set_palette(sns.color_palette(colors))
sns.set_style("dark")

```

3. Summary of Dataset

```
describe = iris.describe()

```

```
all_class_min = iris.groupby(["class"])[["sepal length","sepal width","petal length", "petal width"]].min()

```


```
tfile = open('summary.txt', 'w')
tfile.write("\n")
[...]
tfile.write("\n\nOverview of All Variables:\n")
tfile.write("\n")
tfile.write(describe.to_string())

```

4. Histogram with KDE

```
plt.rc("grid", linestyle="dotted", color="gray", alpha = 0.7)
plt.grid()
ax = sns.histplot(data = iris, x = "sepal width", hue = "class", kde = True, bins = 25, element = "step") 
plt.title("Sepal Width Histogram with Kernel Density Estimate", weight = "bold")
plt.savefig("data-visualizations/histogram - sepal width with density.png") 
plt.show()

```

5. Scatter Plots

```
set_1 = iris[iris["class"] == "Iris-setosa"]
set_2 = iris[iris["class"] == "Iris-versicolor"]
set_3 = iris[iris["class"] == "Iris-virginica"]

```

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


6. Pairplot


```
sns.pairplot(iris, hue = "class", markers = [".", ".", "."], plot_kws = {"alpha": 0.6, "s": 80, "edgecolor": "k"}, height = 2) 
plt.savefig("data-visualizations/pairplot.png")
plt.show()

```

7. Boxplot and Violinplots 


```
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.boxplot(data = iris, palette = "colorblind")
plt.title("Boxplot of Iris Variables", weight = "bold")
plt.savefig("data-visualizations/boxplot - iris.png")
plt.show()

```

```
plt.rc("grid", linestyle = "dotted", color = "gray", alpha = 0.7)
plt.grid()
sns.violinplot(x = "class", y = "sepal length", data = iris)
plt.title("Violinplot of Sepal Length by Class", weight = "bold")
plt.savefig("data-visualizations/violinplot by sepal length - iris.png")
plt.show()

```

# 5. Dataset Analysis

# 6. Why Use Python? 

- free 
- online community + resources
- level of customization 
- sns - quick, easy
- lots of choice of type of plots etc. - can do complex analysis with it - work with complex datasets 
- easily save outputs in other formats you can view, share

# 7. References 

** note - fix referencing formatting ** 

### Introduction 

[1] bezdekIris.data from the University of California at Irvine's machine learning repository. Note: this is the corrected version of the dataset and not the version with two errors. 

### Summary of the Fisher Iris Data Set

[1] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x (accessed 25/03/2021)
[2] https://www.biodiversitylibrary.org/page/16048445#page/470/mode/1up (accessed 25/03/2021)
[3] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735315/ (accessed 25/03/2021)
[4] https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data (accessed 25/03/2021)
[5] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x (accessed 25/03/2021)
[6] https://lucykuncheva.co.uk/papers/jbjkrklknptfs99.pdf (accessed 25/03/2021)
[7] https://archive.ics.uci.edu/ml/datasets/iris (accessed 25/03/2021)

### How to run analysis.py

### Code Explanation

### Dataset Analysis

## Why Use Python? 

## References 
## analysis.py ##
https://www.geeksforgeeks.org/add-column-names-to-dataframe-in-pandas/ (accessed 08/04/2021)
Pandas for Everyone - Daniel Y. Chen
http://makemeanalyst.com/basic-statistics-explore-your-data-cases-variables-types-of-variables/ (accessed 09/04/2021)
https://blogs.helsinki.fi/quantitative-communication/data-gathering/what-is-data/ (accessed 09/04/2021)
https://sphweb.bumc.bu.edu/otlt/mph-modules/bs/bs704_summarizingdata/bs704_summarizingdata_print.html (accessed 09/04/2021)

outputting dataframe to text file - https://stackoverflow.com/questions/32821995/outputting-pandas-dataframe-to-formatted-text-file 
(accessed 10/04/2021)
subplots - https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html (accessed 11/04/2021)
https://stackoverflow.com/questions/52095337/plotting-grids-across-the-subplots-python-matplotlib (accessed 12/04/2021)
https://stackoverflow.com/questions/42372509/how-to-add-a-shared-x-label-and-y-label-to-a-plot-created-with-pandas-plot (accessed 12/04/2021)
https://seaborn.pydata.org/generated/seaborn.displot.html?highlight=displot#seaborn.displot (accessed 12/04/2021)
https://seaborn.pydata.org/tutorial/distributions.html (accessed 13/04/2021)
simple histogram plot - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html (accessed 13/04/2021)
https://datavizcatalogue.com/blog/chart-selection-guide/ (accessed 13/04/2021)
https://seaborn.pydata.org/generated/seaborn.violinplot.html (accessed 13/04/2021)
https://seaborn.pydata.org/generated/seaborn.boxplot.html (accessed 13/04/2021)

# pairplot

http://seaborn.pydata.org/tutorial/aesthetics.html
https://medium.com/@jaimejcheng/data-exploration-and-visualization-with-seaborn-pair-plots-40e6d3450f6d
https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166
https://seaborn.pydata.org/generated/seaborn.pairplot.html (all accessed 22/04/2021)
https://seaborn.pydata.org/tutorial/axis_grids.html