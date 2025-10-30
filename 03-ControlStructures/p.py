name="Ann"
print(name)
print(f"My name is {name}")
print("My name is "+name)

age=int(input('Enter your age: '))
print(f"You are {age}-year old")
print("You are an adult" if age>18 else None)
if age >18:
    print("You are an adult")
else:
    print("You are a child")

for__sale=True
if for__sale:
    print("This item is for sale")
else:
    print("This item isn't for sale")