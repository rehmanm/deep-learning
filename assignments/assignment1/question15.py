

text = input('enter text: ') 

listText = text.split()
dictText = {}

for str in listText:
    currentValue = dictText.get(str, 0)
    dictText[str] =  currentValue + 1

for key, value in sorted(dictText.items()):
    print(key, ':', value)