car_speed=int(input("Enter the speed of the car in km/h: "))
speed_limit_min=40
speed_limit_max=140
if car_speed>speed_limit_min and car_speed<speed_limit_max:
    print("Everything is okay.")
else:
    print("Warning: invalid car speed!!")