number1 = float(input("Enter number one: "))
number2 = float(input("Enter number two: "))
operator = input('Enter symbol: ')
result='Something went wrong'
if operator == '+':
    result = number1+number2
elif operator == '-':
    result = number1-number2
elif operator == '/':
    result = number1/number2
elif operator == '*':
    result = number1*number2
else:
    print('Something is wrong')

# print result
print(f'{number1} {operator} {number2} = {result}')