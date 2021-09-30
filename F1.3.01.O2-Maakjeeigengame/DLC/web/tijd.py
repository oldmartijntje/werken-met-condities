time = 0
while True:
    if time == 0:
        print(str(time)+":00AM")
    elif time > 0 and time < 12:
        print(str(time)+":00AM")
    elif time == 12:
        print(str(time)+":00PM")
    else:
        print(str(time)+":00PM")
    time += 1
    if time == 24:
        break