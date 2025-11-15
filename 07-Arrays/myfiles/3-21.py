arr=[1,2]
arr2=[4,3,1,2,5]
j=0
isSub=False
for i in range(len(arr2)):
    if arr2[i]==arr[j]:
        j+=1
        if j==len(arr):
            isSub=True
            break
    else:
        j=0
print(isSub)