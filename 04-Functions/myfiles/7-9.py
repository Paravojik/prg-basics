def sum(num,even):
    ans=0
    for i in str(num):
        if even:
            if int(i)%2==0:
                ans+=int(i)
        else:
            if int(i)%2==1:
                ans+=int(i)
    return ans
if __name__=="__main__":
    n=int(input("Enter a number: "))
    print(f'f({n},True): {sum(n,True)}')
    print(f'f({n},False): {sum(n,False)}')