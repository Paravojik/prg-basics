def difference(*args):
    min_val=min(args)
    max_val=max(args)
    return max_val - min_val
if __name__=="__main__":
    numbers =[int(x) for x in input("Enter in 1 row 3 numbers: ").split()]
    print(difference(*numbers))