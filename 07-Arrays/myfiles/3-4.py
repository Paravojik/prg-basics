arr=[-15, 8, -31, 47, -2, 19]
def findNum(arr):
    minimum=float('inf')
    maximum=-float('inf')
    for i in arr:
        if i<minimum:
            minimum=i
        if i>maximum:
            maximum=i
    return minimum, maximum
print(findNum(arr))