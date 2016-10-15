import re

text = input('enter text: ')

num = re.findall('[0-9]', text)
print(num)