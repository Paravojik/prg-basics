arr=[(17,15,16,17,15),
 (16,18,19,17,19),
 (19,15,15,19,18),
 (18,17,19,15,16)]

# arr2=[]
# for i in range(len(arr)):
#     crA=list(arr[i])
#     mi=min(crA)
#     ma=max(crA)
#     crA.remove(mi)
#     crA.remove(ma)
#     arr2.append(sum(crA))

# print(arr2)

def sumR(x):
    crA=list(x)
    mi=min(crA)
    ma=max(crA)
    crA.remove(mi)
    crA.remove(ma)
    return sum(crA) 


arr2=list(map(lambda x:sumR(x),arr))
print(arr2)