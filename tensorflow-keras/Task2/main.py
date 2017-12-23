import os
from printGraph import *
from regression_mp import *
from regression import *

os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"

def printMessage():

    print()
    print()
    print("Please Select Appropriate Option")
    print()
    print("****** Menu ******")
    print("1) Reshuffle data")
    print("2) Plot Initial Data in Background")
    print("3) Regression with one parameter y = wx")
    print("4) Regression with multiple parameters y = w0 + w1x")
    print("5) Show Graphs")
    print("0) For Exit")
    print()
    print()

x_train, y_train = getData()

while True:

    printMessage()

    choice = int(input("Please Select: "))
    print()
    print()
    if choice == 1:
        x_train, y_train = getData()
    elif choice==2:
        print("Print Graph")
        plotGraph(x_train, y_train)
    elif choice==3:
        applyRegression(x_train, y_train)
    elif choice == 4:
        applyRegressionMultipleParameters(x_train, y_train)
    elif choice == 5:
        showGraph()

    else:
        print("Thank you for using my code")
        break

