from functools import reduce

numbers = [2,4,6,3,7,5]

numbers=list(filter(lambda x: x%2==0,numbers))

res=reduce(lambda x,y: x+y,numbers)

print(res)