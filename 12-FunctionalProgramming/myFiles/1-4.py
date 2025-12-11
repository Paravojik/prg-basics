a=float(input("Enter speed in m/s: "))



ms_to_kmh=lambda x: x*3.6

res=ms_to_kmh(a)


print(f"{a} m/s = {res} km/h")