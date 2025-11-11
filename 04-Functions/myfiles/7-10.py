def calcCount(start,end):
    return abs(start)//2 if start<0 else 0
if __name__=="__main__":
    a=int(input("Enter start of range: "))
    b=int(input("Enter end of range: "))
    print(f'Number of even numbers in range <{a},{b}> is {calcCount(a,b)}')