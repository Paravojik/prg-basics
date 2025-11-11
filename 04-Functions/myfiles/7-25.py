def summation(x,y):
    ans=0
    for i in range(x,y+1):
        if i%2==0 and i%3==0 and i%4!=0:
            ans+=i
    return ans
if __name__ == "__main__":
    x,y=[int(x) for x in input("Enter two numbers separated by space: ").split()]
    print(summation(x,y))