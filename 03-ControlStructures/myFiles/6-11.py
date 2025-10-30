currentPrice=float(input("Enter the current price of the item: "))
previousPrice=float(input("Enter the previous price of the item: ")) 
discount=100-(currentPrice/previousPrice)*100
if discount>=10:
    print("Buy the product")
    print(f"Product price reduced by {discount}%")