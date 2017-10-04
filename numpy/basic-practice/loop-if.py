print('basic loop of 10 print 0 to 9 using range(10)')
for i in range(10):
    print(i)

print('basic loop of 10 print 0 to 9 using range(0, 10, 2) skip 2')
for i in range(0, 10, 2):
    print(i)


print('basic loop of 10 print 0 to 9 using range(0, 10) and if')
for i in range(0, 10):
    if i % 2 == 0:
        print("Even", i)
    else:
        print("Odd", i)


print('basic loop of 10 print 0 to 9 using range(0, 10) and if')
for i in range(0, 10):
    if i % 2 == 0 and i % 3 == 0:
        print("Even with a multiple of 3", i)
    elif i % 2 == 0:
        print("Even", i)
    else:
        print("Odd", i)

