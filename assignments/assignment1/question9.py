
num = int(input("enter number: "))

result = 0.0
for i in range(1, num+1):
    result = result + i / (i+1)

print("%.2f" % result)