for i in range(1,31):
    if i%5==0 and i%3==0:
        print("BINGO",end=" ")
    elif i%5==0:
        print("FIVE",end=" ")
    elif i%3==0:
        print("THREE",end=" ")
    else:
        print(i,end=" ")