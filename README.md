## Iris Dataset Visualization

Visualization of classic Fisher-Anderson's Iris dataset, which is also available on [Kaggle](https://www.kaggle.com/arshid/iris-flower-dataset).

## Visualization 
Basic plotting :

```python 
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```

## The data

The __iris.csv__ file contains 150 instances of Iris, already labelled with Fisher's classification, considered the golden standard.
The dataset is balanced, i.e., 50 instances for each class.


## The code

In __main.py__ baseline code implements the basic visualisation of the (classified) dataset.

## Task 1:
Populate the following function to show the sepal length vs sepal width scatter plot: 
```python
def scatter_sepal_length_versus_width(data):
    # todo: write the function
    #fig = plt.figure()
    print("scatter_width_versus_length(data): does nothing")
```
## Task 2:
Produce multiple scatter plots in a single figure which contains a grid of 4x4=16 plots. Where, each row is dedicated for a single data dimension (e.g. sepal length) to produce scatter plots vs other three dimensions. For example, copy the following code into the main file and run:

```python
def basic_multiple_scatter_plot(data):
  #Q2: Automate the code to produce a figure of all possible combinations of scatter plots
  #declare subplots with 4X4 dimension. For brevity the demo is for 2X2. Observer (ax1,ax2) is a tuple to hold the plots for the first row. 
  fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2,constrained_layout=True)
    
  colors = ['blue', 'green', 'red']
  #Now here we are plotting in the first row first column 
  ax1.scatter(data[:, 0], data[:,1], c=data[:,4], cmap=matplotlib.colors.ListedColormap(colors))
  #Here we are plotting in the first row second column
  ax2.scatter(data[:, 0], data[:,2], c=data[:,4], cmap=matplotlib.colors.ListedColormap(colors))
  #save
  fig.savefig("iris_multiple_scatter_plot_demo.pdf")
```
Observe the plot. Can you create a 4X4 dimensional scatter plot which compare all the dimensions with each other? 
## Iris in Scikit-Learn

In Scikit-Learn the Iris dataset comes for free as it is often used for testing classification strategies, as illustrated by the following fragment:

```python
# load iris data set from sklearn
from sklearn import datasets

import pandas as pd

iris=pd.DataFrame(datasets.load_iris().data)

# inspect the first 3 rows
iris.head(3)
```
## Plots using seaborn package

### Plot histogram of sepal length dimension in stacked bar
```python
iris=pd.read_csv("iris.csv")
print(iris.head)
#hue is the class separation
sns.histplot(data=iris,  x="SepalLengthCm", hue=iris["Species"], multiple="stack")
plt.show()
```
### Plot histogram of classes of sepal length dimension in three sub plots
```python
iris=pd.read_csv("iris.csv")
g = sns.FacetGrid(iris, col="Species")
g.map(sns.histplot, "SepalLengthCm")
plt.show()
```
### Scatter plot between speal length vs petal length 
```python
iris=pd.read_csv("iris.csv")
g = sns.FacetGrid(iris, hue="Species")
g.map(sns.scatterplot, "SepalLengthCm", "SepalWidthCm", alpha=.7)
g.add_legend()
plt.show()
```
### Plot histograms and scatter plots for all dimensions in one single figure
```python
iris=pd.read_csv("iris.csv")
g = sns.PairGrid(iris, hue="Species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.show()
```