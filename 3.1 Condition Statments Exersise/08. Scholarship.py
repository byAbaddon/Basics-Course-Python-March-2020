# scholarship
# Bug №2 Zero Unitest, but got 100pt
import math

income = float(input())
grade = float(input())
min_salary = float(input())

stipendia = min_salary * 0.35
excellent_sitpemdia = grade * 25

if income < min_salary and grade > 4.5 and grade < 5.5:
      print(f'You get a Social scholarship {math.floor(stipendia)} BGN')
elif grade >= 5.5:
      print(f'You get a scholarship for excellent results {math.floor(excellent_sitpemdia)} BGN')
else:
      print('You cannot get a scholarship!')
  
# 480.00, 4.60, 450.00  
# 300.00, 5.65, 420.00 ~ 141 BGN  mast be 141




