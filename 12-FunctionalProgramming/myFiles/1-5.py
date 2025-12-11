def avg_speed(distance,hours,minutes):
    h=hours+minutes/60
    return distance/h


a1=float(input("Enter distance in km: "))
a2=float(input("Enter number of travel hours: "))
a3=float(input("Enter number of travel minutes: "))

res=avg_speed(a1,a2,a3)
print(f"Average speed: {res:.1f} km/h ")