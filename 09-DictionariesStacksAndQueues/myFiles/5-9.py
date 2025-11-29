vehicle_path='./vehicle.txt'
plates_path='./province.csv'


with open(vehicle_path) as file:
    content=file.read().strip().split('\n')
# print(content)
with open(plates_path, encoding='utf-8') as file:
    plates=file.read().strip().split('\n')
    plates=[i.split(',') for i in plates[1:]]
    plates={i[0]:i[1] for i in plates}
# print(plates)
for i in content:
    if i[0] in plates:
        print(f'{i} is from {plates[i[0]]}')
