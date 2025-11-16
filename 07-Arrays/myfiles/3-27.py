import random
arr=[[random.randint(1,100) for _ in range(4)] for i in range(2)]
print(*arr,sep='\n')

def somePlace(row,column,arr):
    return arr[row-1][column-1]
print(somePlace(2,3,arr))