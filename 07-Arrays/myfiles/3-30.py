arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 

for i in range(5):
    arr[0][i]=i+1
    arr[i][0]=i+1
for i in range(1,5):
    for j in range(1,5):
        arr[i][j]=arr[0][j]*arr[i][0]
print(*arr,sep="\n")
