n1 = int(input("Enter first value:"))
n2 = int(input("Enter second value:"))

# define an anonymous function
mean = lambda x,y: (x+y)/2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {result}")