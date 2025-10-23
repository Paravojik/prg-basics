car_number = input('Enter car registration number: ')
print(f'Car is from Krakow: {car_number[:2]=="KR" or car_number[:2]=="KK"}')