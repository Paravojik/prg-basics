def mean(x,y):
   avg=(x+y)/2
   return avg

# takes two numbers from keyboard
n1 = int(input("Enter first value:"))
n2 = int(input("Enter second value:"))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')