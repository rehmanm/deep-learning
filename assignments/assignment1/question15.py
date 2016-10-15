

text = 'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3'

listText = text.split()
dictText = {}

for str in listText:
    currentValue = dictText.get(str)
    if(currentValue == None):
        currentValue = 0
    dictText[str] =  currentValue + 1

for key, value in sorted(dictText.items()):
    print(key, ':', value)