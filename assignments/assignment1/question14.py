import math

def move():
    text = input("enter move e.g. UP 5:").split(' ')
    print (text)
    str = text[0].upper()
    displacement = int(text[1])
    if (str == "UP"):
        return (0, displacement)
    elif (str == "DOWN"):
        return (0, -1 * displacement)
    elif (str == "RIGHT"):
        return (displacement, 0)
    else:
        return (-1 * displacement, 0)

def distance(point1, point2):
    return int(math.sqrt(math.pow(point2[0] - point1[0], 2) + pow(point2[1] - point1[1], 2)))

startPos = (0,0)
currentPos = (0,0)

points = []
points.append(startPos)
addPoints = True

while addPoints:
    newPos = move()
    currentPos = (currentPos[0] + newPos[0], currentPos[1] + newPos[1])
    points.append(newPos)
    addPoints = input("add move Default 'Y' (Y/N):").upper() != "N"

print(points)
print(startPos, currentPos, distance(startPos, currentPos))

