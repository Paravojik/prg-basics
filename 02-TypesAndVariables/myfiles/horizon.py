import math
height=float(input('Enter your height in metres: '))
d=3.57* math.sqrt(height)
print(f"you can see the horizon only in {round(d,3)}km")