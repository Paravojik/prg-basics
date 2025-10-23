cm=float(input("Enter height in cm: "))
feet=int(cm/30.48)
inches=(cm%30.48)/2.54
print(f'Height in feet and inches: {feet} ft {round(inches,2)} in')