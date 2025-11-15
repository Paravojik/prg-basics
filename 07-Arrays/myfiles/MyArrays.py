def secondLargest(arr):
    arr=arr.copy()
    a=max(arr)
    arr.remove(a)
    return max(arr)


def difference(arr):
    return max(arr)-min(arr)


def median(arr):
    arr=arr.copy()
    n=len(arr)
    arr.sort()
    if n%2==0:
        val=arr[n//2-1]+arr[n//2]/2
        return val
    else:
        return arr[n//2]
def minaAndMax(arr):
    return (min(arr),max(arr))


def retArr(arr):
    return "-".join(map(str,arr))
