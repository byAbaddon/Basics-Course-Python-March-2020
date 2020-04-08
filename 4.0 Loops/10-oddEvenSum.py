#oddEvenSum
loop = int(input())
even_sum = 0
odd_sum = 0
list_num = []

while loop > 0 :
    list_num.append(int(input()))
    loop -= 1  

for i in range(len(list_num)):
    if i % 2 == 0:
      even_sum += list_num[i]
    else:
      odd_sum +=  list_num[i]
  
if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
  print(f'No\nDiff = {abs(even_sum - odd_sum)}')
   

# 4, 10, 50, 60, 20  //yes