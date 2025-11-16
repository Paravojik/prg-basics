import random
arr=[[random.randint(1,100) for i in range(5)] for _ in range(3)]

print(*arr,sep="\n")
arr[0],arr[-1]=arr[-1],arr[0]
print("-------------")
print(*arr,sep="\n")