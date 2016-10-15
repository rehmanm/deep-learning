text = input('enter text: ')

listText = list(text)

newListText = []
for str in listText[::2]:
    newListText.append(str)

print(''.join(newListText))