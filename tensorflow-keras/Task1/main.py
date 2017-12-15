import os
from areaOfCircle import AreaOfCircle
from areaOfRectangle import AreaOfRectangle

os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"

def printMessage():

    print()
    print()
    print("Please Select Appropriate Option")
    print()
    print("****** Menu ******")
    print("1) Area Of Circle")
    print("2) Area Of Rectangle")
    print("0) For Exit")
    print()
    print()



while True:

    printMessage()

    choice = int(input("Please Select: "))
    print()
    print()
    if choice==1:
        c = AreaOfCircle()
        c.calculateAreaandRadius()
    elif choice==2:
        r = AreaOfRectangle()
        r.calculateAreaandRadius()
    else:
        print("Thank you for using my code")
        break



