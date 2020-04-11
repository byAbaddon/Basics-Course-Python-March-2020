#cake
import sys
w_part = int(input()) 
l_part =int(input())
birthday_cake = w_part * l_part
pieces = int(input())

while pieces != 'STOP':
    birthday_cake -= int(pieces)
    if birthday_cake <= 0:
      print(f'No more cake left! You need {abs(birthday_cake)} pieces more.')
      sys.exit()
    pieces = input()

print(f'{birthday_cake} pieces are left.') 

#10, 10, 20, 20, 20, 20, 21
