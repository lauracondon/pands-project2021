# Table of Contents

1. Introduction
2. History and Contents of the Fisher Iris Data Set
3. How to run analysis.py
4. Software and Libraries Used
5. Code Explanation
6. Why Python? 
7. References 

# Introduction

This github repository contains my final project for the 2021 Programming and Scripting module for GMIT's HDip in Science in Computing (Data Analytics).

Along with this README which will explain the project in detail, this repository contains the following: 

- data-visualizations - this folder contains all png files outputted by analysis.py.
- analysis.py - this Python file contains all the code used to analyse the iris dataset.
- iris.data - the version of the Fisher Iris dataset used for this project [1]. 
- summary.txt - this text file contains various numerical summaries of the variables in the     iris dataset as outputted by analysis.py. 

# History and Contents of the Fisher Iris Data Set

The Fisher Iris data set is a multivariate data set consisting of a total of one hundred and fifty samples of iris flowers. Fifty samples were collected from each of three different species of iris (iris setosa, iris virginica and iris versicolor) by Edgar Anderson. Four attributes are recorded for each sample - sepal length, sepal width, petal length, petal width - as well as the class identifier (the species of the iris). All measurements are given in centimeters [1]. 

R.A. Fisher first published this dataset in the article 'The Use of Multiple Measurements in Taxonomic Problems' in 1936. In it, Fisher uses the dataset to create a linear discriminant model in order to classify the three different species of iris. Anderson also published an article in 1936, entitled 'The Species Problem in Iris' in which he uses the information from the dataset, in combination with additional research, to hypothesize that iris versicolor is an amphidiploid hybrid of iris setosa and iris virginica [2]. This hypothesis was confirmed by Yoong Lim et. al in 2007 in the article 'Parental Origin and Genome Evolution in the Allopolyploid Iris versicolor' [3]. 

Since its publication, Fisher's iris dataset has become tremendously popular for use in machine learning and statistics. According to Wiley Online Library, it has been cited in other publications 7,422 times [5].  

Use of this dataset is not without issue, however, and there are errors that were incorporated into its reproduced versions which went unnoticed for many years. Notably, the version uploaded to the University of California at Irvine's machine learning repository contains two errors, as first noted by Besdek et. al [6].  These errors are now acknowledged by the UCI on their website [7]. Additionally some biologists have argued that iris flowers don't actually have sepals at all and instead have tepals [8]. That argument is best left to them but it is an interesting aside to a near ubiquitous dataset. 

# How to run analysis.py

# Software and Libraries Used

# Code Explanation

# Why Python? 

# References 

** note - fix referencing formatting ** 

## Introduction 

[1] bezdekIris.data from the University of California at Irvine's machine learning repository. Note: this is the corrected version of the dataset and not the version with two errors. 

## History and Contents of the Fisher Iris Data Set

[1] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x (accessed 25/03/2021)
[2] https://www.biodiversitylibrary.org/page/16048445#page/470/mode/1up (accessed 25/03/2021)
[3] https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735315/ (accessed 25/03/2021)
[4] https://www.researchgate.net/publication/237010807_What_should_we_know_about_the_famous_Iris_data (accessed 25/03/2021)
[5] https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x (accessed 25/03/2021)
[6] https://lucykuncheva.co.uk/papers/jbjkrklknptfs99.pdf (accessed 25/03/2021)
[7] https://archive.ics.uci.edu/ml/datasets/iris (accessed 25/03/2021)

## How to run analysis.py

## Software and Libraries Used

## Code Explanation

## Why Python? 

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