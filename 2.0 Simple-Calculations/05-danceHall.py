from math import floor

arg_L = float(input())
arg_W = float(input())
arg_A = float(input())

hall = (arg_L * 100) * (arg_W  * 100)           
checkroom = ((arg_A* 100) * (arg_A * 100))    
bench = hall / 10
dance_space = 40 + 7000
free_space = hall - (checkroom + bench)
print(f'{floor(free_space / dance_space)}')


