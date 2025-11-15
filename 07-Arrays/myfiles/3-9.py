def check(arr1,arr2):
    return arr1==arr2
print(check([1,2,3],[1,2,3]))
print(check(["water","book","sky"], ["water","book","sky"]))
print(check([True, False], [True, False, True]))
print(check([5, 3, 1], [5, 3, 1]))
print(check([3, 2, 1], [3, 2]))


print(check([5, 3, 1], [5, 3, 2]))
