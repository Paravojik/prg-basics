temperatures = [
 3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
 4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
 -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]
measurements = len(temperatures)
total_temp = 0
negative_days = 0

for i in temperatures:
    total_temp+=i
    if i<0:
        negative_days+=1
average_temp = total_temp / measurements
min_temp=min(temperatures)
max_temp=max(temperatures)




print('TEMPERATURE REPORT')
print('Month: March')
print('Number of measurements:',measurements)
print('Average temperature:', round(average_temp,2))
print('Minimum temperature:', min_temp)
print('Maximum temperature:', max_temp)
print('Number of negative temperature days:', negative_days)