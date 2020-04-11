#graduationTwo
import sys

name = input()
grade = 0
count_class = 1

for _ in range(0,12):
    el = float(input()) 
    if el >= 4.00:
        grade += el
        count_class += 1
    elif el < 2.1:
        print(f'{name} has been excluded at {count_class} grade')
        sys.exit()   
                 
print(f'{name} graduated. Average grade: {(grade / 12):.2f}');

#Mimi', '5', '6', '5', '6', '5', '6', '6', '2', '3' 