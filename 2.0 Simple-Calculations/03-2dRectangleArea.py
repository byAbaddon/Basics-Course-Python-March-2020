import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

height = abs(x1 - x2)
width =  abs(y1 - y2)
print(f'{(height * width):.2f}')
print(f'{(height * 2) + (width * 2):.2f}')



