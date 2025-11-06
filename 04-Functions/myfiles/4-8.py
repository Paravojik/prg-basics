def time_string(hours, minutes, time_format):
    if minutes<10:
        minutes='0'+str(minutes)
    if time_format=="24":
        if hours<10:
            return f"0{hours}:{minutes}"
        else:
            return f"{hours}:{minutes}"
    else:
        if hours==0:
            return f"12:{minutes}am"
        elif hours==12:
            return f"12:{minutes}pm"
        elif hours<12 and hours>0:
            return f"{hours}:{minutes}am"
        elif hours>12 and hours<=23:
            return f"{hours%12}:{minutes}pm"
        else:
            return None
print(time_string(15, 38, '24'))  # 15:38
print(time_string(8, 3, '24'))    # 08:03
print(time_string(0, 5, '24'))    # 00:05
print(time_string(11, 15, '12'))  # 11:15am
print(time_string(0, 7, '12'))    # 12:07am
print(time_string(7, 30, '12'))   # 7:30am
print(time_string(12, 46, '12'))  # 12:46pm
print(time_string(13, 10, '12'))  # 1:10pm
print(time_string(19, 2, '12'))   # 7:02pm