hour=int(input('Enter the number of hours: '))
if hour<1:
    print("It is free")
elif hour>=1 and hour<=2:
    print("The fee is 5 PLN")
elif hour>=3 and hour<=6:
    print("The fee is 15 PLN")
else:
    print("The fee is 20 PLN")
