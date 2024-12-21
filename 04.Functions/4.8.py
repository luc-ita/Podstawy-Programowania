def time_string(hours, minutes, time_format):
    if time_format == 12:
        if hours >= 12:
            hours = hours - 12
            return f'{hours}:{minutes}pm'
        else:
            return f'{hours}:{minutes}am'
    elif time_format == 24:
        return f'{hours}:{minutes}'
while True:
    hours = int(input("Enter hours: "))
    if hours <= 23 and hours >= 0:
        break
while True:
    minutes = int(input("Enter minutes: "))
    if minutes <= 59 and minutes >= 0:
        break
while True:
    time_format = int(input('Enter time format 12or24: '))
    if time_format == 12 or time_format == 24:
        break
print(f"Time is: {time_string(hours,minutes,time_format)}")