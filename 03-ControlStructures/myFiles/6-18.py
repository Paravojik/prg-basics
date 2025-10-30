x=int(input("Enter x: "))
y=int(input("Enter y: "))
if x>0 and y>0:
    print("Point is in the first quadrant.")
elif x<0 and y>0:
    print("Point is in the second quadrant.")
elif x<0 and y<0:
    print("Point is in the third quadrant.")
elif x>0 and y<0:
    print("Point is in the fourth quadrant.")   
elif x==0 and y==0:
    print("Point is at (0,0).")
elif x==0:
    print("Point is on the Y axis.")
elif y==0:
    print("Point is on the X axis.")