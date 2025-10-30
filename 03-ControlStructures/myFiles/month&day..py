month = int(input('Enter month number (1..12)'))
day = int(input('Enter the day number of the month: '))
day_ok = False

if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and day<=31 :
    day_ok=True ## months with 31 days
elif month==2 and day<=28:
    day_ok=True  ## months with 30 days
elif day<=30 and month!=2:
     day_ok=True 
## February 28 days 

message = f'Day {day} for the month {month}'
if day_ok:
    print(f'{message} is correct')
else:
    print(f'{message} is incorrect')