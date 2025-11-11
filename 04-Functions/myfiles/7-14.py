def calcSMTH(a,b,sym):
    match sym:
        case '+':
            return a+b
        case '-':
            return a-b
        case '*':
            return a*b
        case '/':
            return a/b 
        case "**":
            return a**b
        case _:
            return "Invalid operation"
if __name__=="__main__":
    x=int(input("Enter first number: "))
    y=int(input("Enter second number: "))
    operation=str(input("Enter operation (+, -, *, /, **): "))
    result=calcSMTH(x,y,operation)
    print(f'Result: {result}')