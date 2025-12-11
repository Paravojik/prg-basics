a=str(input("Enter your name: "))
b=str(input("Enter your surname: "))


initials=lambda name, surname: name[0].upper()+surname[0].upper()

res=initials(a,b)


print(f"Your initials: {res}")