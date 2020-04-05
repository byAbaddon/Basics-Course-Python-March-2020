# function timeAddMinutes
hours = int(input())
min = int(input())

min += 15

if min >= 60:
    min -= 60
    hours += 1

if hours >= 24:
    hours -= 24

if min < 10:
    print(f"{hours}:0{min}")
else:
    print(f"{hours}:{min}")

# 11, 08

