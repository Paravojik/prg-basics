code=str(input("Enter EAB-13: "))
if len(code)==13:
    print("Valid EAB-13")
    if code[0:3]=="590":
        print("Product is from Poland")
