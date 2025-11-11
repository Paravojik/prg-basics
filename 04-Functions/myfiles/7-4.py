text=str(input("Enter text: "))
def calcSymbols(sym,text):
    count=0
    for i in text:
        if i==sym:
            count+=1
    return count
symbol=str(input("Enter symbol to count: "))
result=calcSymbols(symbol,text)
print(f'The number of letter "{symbol}": {result}')