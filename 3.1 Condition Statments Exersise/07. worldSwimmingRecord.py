# swimmingRecord
import math

record = float(input())
trace = float(input())
metersMin = float(input())
  
swiming_trace = trace * metersMin
add_seconds = math.floor(trace / 15) * 12.5 
time = swiming_trace + add_seconds
  
if time >= record:
    time = abs(record - time)
    print(f'No, he failed! He was {time:.2f} seconds slower.')
else:
    print(f'Yes, he succeeded! The new world record is {time:.2f} seconds.')
  

# 10464, 1500, 20
# 55555.67, 3017, 5.03
