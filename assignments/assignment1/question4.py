text = input("enter text:")

listText = list(text)

dictText = {}
for str in listText:
    currentValue = dictText.get(str)
    if(currentValue == None):
        currentValue = 0
    dictText[str] =  currentValue + 1

for key, value in dictText.items():
    print(key, ',', value)