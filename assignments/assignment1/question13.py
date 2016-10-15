class myClass:

    def divisibleby7(self, n):
        num = 0
        while num < n:
            if(num % 7 == 0):
                yield num
            num += 1


x = myClass()
for x in x.divisibleby7(100):
    print(x)