text = input('enter text: ')

listText = list(text)

reverseListText = []
for str in listText[::-1]:
    reverseListText.append(str)

print(''.join(reverseListText))