def isRight(code):
    summation=int(code[0])+int(code[1])+int(code[2]) 
    return True if summation%7==int(code[3]) else False
if __name__ == "__main__":
    code=str(input("Enter the 4-digit code: "))
    print(isRight(code))
