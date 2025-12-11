a1=float(input("Enter distance in km: "))
a2=float(input("Enter number of travel hours: "))
a3=float(input("Enter number of travel minutes: "))


avg_speed=lambda distance,hours,minutes: distance/(hours+minutes/60)


res=avg_speed(a1,a2,a3)
print(f"Average speed: {res:.1f} km/h ")