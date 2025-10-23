height=int(input('Enter your height in sm: '))
weight=int(input('Enter your wight in kg: '))
bmi=weight/(height/100)**2
bmi=round(bmi,2)
print('Your BMI is', bmi)
print('Check on the Internet if your BMI is ok!!')