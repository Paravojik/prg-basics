num=int(input("Enter a number of products purchased: "))
price=float(input("Enter a price: "))
print("Amount to pay: ",min(num,2)*price+max(0,num-2)*price*0.75)