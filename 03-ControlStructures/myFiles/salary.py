basic_salary = 5000
total_salary = 0
bonus = 0.3 # 30%
is_bonus = input('Does the employee receive a bonus? (Y/N):') == 'Y'

if is_bonus:
    total_salary = basic_salary*bonus+basic_salary
else:
    total_salary=basic_salary

print(f'Basic salary: {basic_salary}')
print("Bonus included? " +"Yes" if is_bonus==True else "Bonus included? No")
print(f'Total salary: {total_salary}')