import time
days = int(input("Input the amount of days: "))
hours = int(input("Input the amount of hours: "))
minutes = int(input("Input the amount of minutes: "))
seconds = int(input("Input the amount of seconds: "))

total_seconds = 0
total_seconds += days * 86400
total_seconds += hours * 3600
total_seconds += minutes * 60
total_seconds += seconds

print("The time in seconds is", total_seconds)

second = int(input("Input the amount of time in seconds: "))
day = 0
hour = 0
minute = 0
second1 = 0

while second != 0:
    if second >= 86400:
        second -= 86400
        day += 1
    elif second >= 3600:
        hour += 1
        second -= 3600
    elif second >= 60:
        minute += 1
        second -= 60
    else:
        second1 += 1
        second -= 1
lst = []
lst.append(day)
lst.append(hour)
lst.append(minute)
lst.append(second1)

for i in range(1, 4):
    if lst[i] < 10:
        lst[i] = "0" + str(lst[i])
    lst[i] = str(lst[i])
    lst[0] = str(lst[0])

print( lst[0] + ":" + lst[1] + ":" + lst[2] + ":" + lst[3] )

time_now = time.asctime()
print(time_now)