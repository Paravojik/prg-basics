def sumNatural(n):
    if n==1:
        return 1
    else:
        return n+sumNatural(n-1)
if __name__ == "__main__":
    n=int(input("Enter a number: "))
    print(sumNatural(n))