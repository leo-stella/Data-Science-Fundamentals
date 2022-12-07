import csv
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


def import_iris(ifname):
    """
        Imports data with file-name/-path ifname as a numpy array.
    """
    classes = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    with open(ifname, 'r') as ifname:
        # read data using csv reader object which is a list of rows
        datareader=csv.reader(ifname, delimiter=",")
        # we want to avoid importing the header line.
        # instead we'll print it to screen
        header=next(datareader)
        # CSV reader reads data as strings. We need to process them
        data=[]  # to store processed data
        for row in datareader:
            # Convert the strings for a row into floats
            # Omit the first column as it is an index of a row
            # Omit the last comlumn as it is the class name
            row_of_floats=list(map(float, row[1:5]))
            # Process class name separately
            # Insert a number instead of class name
            class_of_this_row=classes.index(row[5])
            # Now append the processed class into the row
            row_of_floats.append(class_of_this_row)
            # Now store in our data list
            data.append(row_of_floats)
        # convert the data (list object) into a numpy array.
        data_as_array = np.array(data)

        # return this array to caller
        return data_as_array


def histogram_sepal_width(data):
    # create an empty figure object
    fig = plt.figure()
    # create a single axis on that figure
    ax = fig.add_subplot(1,1,1)
    # todo: histogram the data and label the axes
    plt.hist(data[:,1])
    # ax.set_xlabel("Change me please")
    # ax.set_ylabel("Change me please")
    ax.set_xlabel("Sepal Width")
    ax.set_ylabel("Count")
    fig.savefig("iris_sepal_width_histogram.pdf", fmt="pdf")


def scatter_sepal_length_versus_width(data):
    fig = plt.figure()
    # create a single axis on that figure
    ax = fig.add_subplot(1, 1, 1)
    # histogram the data and label the axes
    colors = ['blue', 'green', 'red']
    plt.scatter(data[:, 0], data[:,1], c=data[:,4], cmap=matplotlib.colors.ListedColormap(colors))
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    fig.savefig("iris_sepal_length_versus_width_scatter.pdf", fmt="pdf")


def basic_multiple_scatter_plot(data):
    # Q2: Automate the code to produce a figure of all possible combinations of scatter plots
    # declare subplots with 4X4 dimension.
    # For brevity the demo is for 2X2. Observer (ax1,ax2) is a tuple to hold the plots for first row.
    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, constrained_layout=True)
    fig, ax=plt.subplots(4, 4, constrained_layout=True)
    # ax1 = fig.add_subplot(1, 1, 1)
    colors = ['tab:blue', 'tab:green', 'tab:red']
    titles=["Sepal Length","Sepal Width","Petal Length","Petal Width"]
    # i,j are column and row respectively
    for i in range(0,4):
        for j in range(0,4):
            # In (0,0), (1,1), (2,2) and (3,3) grids scatter plots are not generated
            if i==j:
                ax[i][j].plot()
                ax[i][j].set_xlabel(titles[i])
                ax[i][j].set_ylabel(titles[j])
                anchored_text = AnchoredText(titles[i], loc=2)
                ax[i][j].add_artist(anchored_text)
            else:
                # For each data dimension i scatter plot with other dimension j
                ax[i][j].scatter(data[:, i], data[:,j], c=data[:,4], cmap=matplotlib.colors.ListedColormap(colors))
                ax[i][j].set_xlabel(titles[i])
                if j==0:
                  ax[i][j].set_ylabel(titles[j])
    fig.savefig("iris_multiple_scatter_plot.pdf")


def main(ifname):
    data = import_iris(ifname)
    print(data[0])
    if type(data) == np.ndarray:
        print("Data array loaded: there are %d rows" % data.shape[0])

    # include calls to any functions you write.
    histogram_sepal_width(data)
    scatter_sepal_length_versus_width(data)
    basic_multiple_scatter_plot(data)

    plt.show()


if __name__ == '__main__':
    # this allows you to pass the file name as the first argument when you call
    # your script from the command line
    # so to run this script use:
    # python iris.py Iris.csv
    main('iris.csv')