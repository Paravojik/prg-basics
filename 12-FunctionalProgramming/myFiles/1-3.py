def ms_to_kmh(ms):
    return ms*3.6


a=float(input("Enter speed in m/s: "))

res=ms_to_kmh(a)

print(f"{a} m/s = {res} km/h")