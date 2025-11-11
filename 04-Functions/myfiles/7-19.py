def calcVal(num):
    arr={int(x):0 for x in range(0,10)}
    for char in str(num):
        digit=int(char)           
        arr[digit]+=1
    ans=0
    for i in arr:
        if arr[i] > 1:
            ans+=arr[i]*i
    return ans
if __name__=="__main__":
    number=int(input("Enter a number: "))
    print(calcVal(number))
