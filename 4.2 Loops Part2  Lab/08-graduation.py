#graduation
name = input()        
grade = 0
count = 0

while count < 12:
    el = float(input())
    if el >= 4.0:
        grade += el
        count += 1
    
print(f'{name} graduated. Average grade: {grade / 12 :.2f}')

#Ani, 5, 5.32, 6, 5.43, 5, 6, 5.5, 4.55, 5, 6, 5.56, 6
