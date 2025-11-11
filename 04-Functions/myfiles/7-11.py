def isNegative(*args):
    for num in args:
        if num<0:
            return True
    return False
if __name__=="__main__":
    numbers =[int(x) for x in input("Enter in 1 row 3 numbers: ").split()]
    print(f'At least one number is negative: {"yes" if isNegative(*numbers) else "no"}')