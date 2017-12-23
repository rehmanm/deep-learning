import numpy as np
#import matplotlib
#matplotlib.use('agg')
import matplotlib.pyplot as plt

def getData():
    x_train = np.linspace(-1, 1, 101)
    y_train = 2 * x_train + np.random.randn(x_train.size) * 0.33
    return (x_train, y_train)

def plotGraph(x_train, y_train):
    fig = plt.figure(1)
    fig.clear()
    #x_train, y_train = getData()
    plt.scatter(x_train, y_train, marker = 'x', color='r')
    plt.draw()

def showGraph():
    plt.show()


