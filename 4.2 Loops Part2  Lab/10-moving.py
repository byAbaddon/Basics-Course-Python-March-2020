#moving
import sys
a ,b ,c  = int(input()), int(input()), int(input())
free_space = a * b * c
cubic_mt = 0

el = input()
while el != 'Done' and  free_space > cubic_mt:
    
    cubic_mt += int(el)
    if free_space < cubic_mt:
      break
    el = input()
   
if free_space < cubic_mt:
    print(f'No more free space! You need {abs(free_space - cubic_mt)} Cubic meters more.')
         
else:
    print(f'{(free_space - cubic_mt)} Cubic meters left.')
      
#10, 1, 2, 4, 6, Done            
    
    
    









   

   



  





#10 , 1, 2, 4, 6, Done

 
 
 
  

