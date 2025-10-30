driving_mode = input('Enter driving mode (A/M/E): ')

if driving_mode == 'A':
    fuel_consumption = 7 # liters per 100km
elif driving_mode == 'M':
    fuel_consumption = 9 # liters per 100km  
elif driving_mode == 'E':
    fuel_consumption = 6 # liters per 100km  
else:
    print("Incorect symbol")


distance = int(input('Enter distance in km: '))
fuel_consumption=0

total_consumption = fuel_consumption*distance/100
print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption} liters')