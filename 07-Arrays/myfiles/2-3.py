monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]




print('MONTHLY EXPENSES')
print('----------------')
print('Food:', sum(week[0] for week in monthly_expenses))
print('Transport:', sum(week[1] for week in monthly_expenses))
print('Utilities:', sum(week[2] for week in monthly_expenses))
print('Week 1:', sum(monthly_expenses[0]))
print('Week 2:', sum(monthly_expenses[1]))
print('Week 3:', sum(monthly_expenses[2]))
print('Week 4:', sum(monthly_expenses[3]))
print('---------------')
print('TOTAL:', sum(sum(week) for week in monthly_expenses))