def draw(n):
    return '*/'*(n-1)+"*" if n>0 else ''
if __name__=="__main__":
    num=int(input("Enter a number: "))
    print(draw(num))