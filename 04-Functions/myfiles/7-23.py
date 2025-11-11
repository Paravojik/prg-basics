def password(passw):
    if len(passw)<6:
        return False
    appeared=[]
    for i in passw:
        if i in appeared:
            return False
        appeared.append(i)
    return True
if __name__=="__main__":
    pwd=str(input("Enter a password: "))
    print(password(pwd))