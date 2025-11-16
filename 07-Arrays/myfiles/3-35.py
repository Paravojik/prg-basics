def transpose_natrix(arr):
    return [[arr[i][j] for i in range(len(arr))] for j in range(len(arr[0]))]
def showArr(arr):
    for i in arr:
        print(" ".join(map(str,i)))


showArr(transpose_natrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print("-----")
showArr(transpose_natrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]))
print("-----")


showArr(transpose_natrix([[5, 6, 7, 8]]))