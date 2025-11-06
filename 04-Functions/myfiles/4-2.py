def digitsCal(a):
    ans=0
    a=str(abs(a))
    for i in range(len(a)):
        ans+=int(a[i])
    return ans
print(digitsCal(int(input("Enter a number: "))))