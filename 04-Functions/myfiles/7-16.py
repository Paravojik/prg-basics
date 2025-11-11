def fibonaci(n):
    a,b=0,1
    ans=[]
    for i in range(n):
        ans.append(a)
        a,b=b,a+b
    return ans[-1]
if __name__=="__main__":
    num=int(input("Enter a number: "))
    print(fibonaci(num))