def calExpression(exp):
    ans=int(exp[0])
    for i in range(1,len(exp),2):
        if exp[i]=='+':
            ans+=int(exp[i+1])
        else:
            ans-=int(exp[i+1])
    return ans

if __name__=="__main__":
    expression=str(input("Enter the expression: "))
    print(calExpression(expression))