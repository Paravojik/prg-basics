import math
def triangle_area(a,b,c):
    p=(a+b+c)/2
    S=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return S
print(triangle_area(3,4,5))
print(triangle_area(5, 12, 13 ))
print(triangle_area(7, 24, 25))