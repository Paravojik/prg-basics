def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
if __name__ == "__main__":
    a=int(input("Enter the base number: "))
    b=int(input("Enter the exponent number: "))
    print(power(a,b))