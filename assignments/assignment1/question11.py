import re

def validatePassword(password):
    objections = []
    if(len(password) <6):
        objections.append("password should be minimum 6 characters")
    if (len(password) > 12):
        objections.append("password should be maximum 12 characters")
    if (len(re.findall('[a-z]',password)) == 0):
        objections.append("password should contain atleast one small alphabet")
    if (len(re.findall('[A-Z]',password)) == 0):
        objections.append("password should contain atleast one capital alphabet")
    if (len(re.findall('[$#@]',password)) == 0):
        objections.append("password should contain atleast one special character from [$#@]")
    if (len(re.findall('[0-9]',password)) == 0):
        objections.append("password should contain atleast one digit")
    return objections


passwords = input("enter password list ',' seperated: ").split(',')


for password in passwords:
    objections = validatePassword(password)
    if(len(objections) == 0):
        print (password)


