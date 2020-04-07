#operationsBetweenNumbers
x = int(input())
y = int(input())
operator = input()

def calc(x, y, operator):
    result = 0
    if operator == '+':
        result = x + y   
    elif operator == '-':  
        result = x - y 
    elif operator == '*':  
        result = x * y 
    elif operator == '/':
       try:
           result = x / y
       except ZeroDivisionError:
            result = 0   
    elif operator == '%':
       try:
           result = x % y
       except ZeroDivisionError:
            result = 0   
    if operator == '+' or operator == '-' or operator == '*':
       isEven  = 'even' if result % 2 == 0 else 'odd'
       return  print(f'{x} {operator} {y} = {result} - {isEven}')
    else:   
       if result == 0: 
          return print(f'Cannot divide {x} by zero')
       elif operator == '/':
          return  print(f'{x} {operator} {y} = {result:.2f}')
       else:  
          return  print(f'{x} {operator} {y} = {result}')

calc(x, y, operator)    

#10, 12, +
#10, 0, %