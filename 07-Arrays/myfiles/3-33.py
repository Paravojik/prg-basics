def identity_matrix(n):
    return [ [1 if i==j else 0 for i in range(n)] for j in range(n)]
def showArr(arr):
    for i in arr:
        print(" ".join(map(str,i)))
showArr(identity_matrix(3))
print("-----")
showArr(identity_matrix(5))
print("-----")
showArr(identity_matrix(8))
print("-----")