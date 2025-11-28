import re

def checkUsername(username):
    pattern=r'^[a-z]{6,}$'
    if re.match(pattern,username):
        return True
    return False
def checkPassword(password):
    pattern=r'^[\w_]{8,}$'
    if re.match(pattern,password):
        return True
    return False
username=input("Enter username: ")
password=input("Enter password: ")

if checkUsername(username):
    print("Username is valid")
else:
    print("Username is invalid")    
    
if checkPassword(password):
    print("Password is valid")
else:
    print("Password is invalid")  