def create_2d_arr(x,y):
    return [[0 for i in range(y)] for j in range(x)]


print(*create_2d_arr(3,5),sep="\n")