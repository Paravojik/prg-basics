arr=[1,5,1223,7.62,34,23.56,5,7,89]
print(arr)
a=float(input("Enter a number: "))
print(len([i for i in arr if i>a]))