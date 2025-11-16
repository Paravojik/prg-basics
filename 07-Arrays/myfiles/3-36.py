def d2Tod1(arr):
    return [arr[i][j] for i in range(len(arr)) for j in range(len(arr[0]))]

print(d2Tod1([[2, 3],[1, 5]]))
print(d2Tod1([[5, 0, 3, 7, 5], [9, 0, 9, 1, 2]]))
print(d2Tod1([[2, 1],
[3, 5],
[7, 4],
[2, 6]]))