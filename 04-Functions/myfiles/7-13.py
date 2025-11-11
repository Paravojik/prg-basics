def draw(n):
    ans=""
    for i in range(n):
        ans+=str(i+1)
    return ans
if __name__=="__main__":
    num=int(input("Enter a number: "))
    print(draw(num))