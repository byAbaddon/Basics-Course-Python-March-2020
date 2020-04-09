#halfSumElement
from functools import reduce

loop = int(input())
num_list = []

while loop > 0:
    num_list.append(int(input()))
    loop -= 1

big_num = max(num_list)
sum_all_num = reduce(lambda a, b: a + b, num_list) - big_num
print(f'Yes\nSum = {big_num}' if sum_all_num == big_num  else f'No\nDiff = {abs(sum_all_num - big_num)}')

#3, 5, 5, 1 
       
        
        
   
        
        
    
             