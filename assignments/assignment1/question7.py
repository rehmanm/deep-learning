import re

email = input("enter email: ")

username = re.search('\w+', email)

print (username.group(0))