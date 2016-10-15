def f(n):
    if(n > 0):

        if (n > 1):
            return 100 + f(n-1)
        else:
            return 100
    elif (n == 0):
        return 1



num =  int(input('enter number: '))

print(f(num))
