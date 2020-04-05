from datetime import datetime, timedelta

a = int(input())
b = int(input())
c = int(input())

list = (a, b, c)
result = sum(list)

time = datetime(2020, 3, 22) 
delta = timedelta( seconds = result)
print(str(delta)[slice(3, 10)])


# 35,45,44
# 22,7,34
# 50,50,49
# 14,12,10
