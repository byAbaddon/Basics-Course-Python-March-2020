# metricConverter
n = float(input())
first = input()
second = input()

if first == "mm":
    number_mm = n
elif first == "cm":
    number_mm = n * 10
else:
    number_mm = n * 1000
 
if second == "mm":
    output = number_mm
elif second == "cm":
    output = number_mm / 10
else:
    output = number_mm / 1000
 
print(f"{output: .3f}")
 
 
#'12', 'mm',  'm'
