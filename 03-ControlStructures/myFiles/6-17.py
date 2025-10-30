time=input("Enter time (24-hour format): ")
time12=str(int(time[:2])%13) + time[2:]
am_pm="AM" if int(time[:2])<12 else "PM"
print(f"Time in 12-hour format: {time12}{am_pm}")