text = input("enter text:")

listText = list(text)

dictText = {}
for str in listText:
    currentValue = dictText.get(str, 0)
    dictText[str] =  currentValue + 1

for key, value in dictText.items():
    print(key, ',', value)