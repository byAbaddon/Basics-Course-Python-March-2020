#accountBalance
n = int(input())
total_sum = 0

for _ in range(0, n):
   sum_in = float(input())
   if sum_in >= 0:
      total_sum += sum_in
      print(f'Increase: {sum_in:.2f}') 
   else:
      print(f'Invalid operation!');
      break
    
print('Total:', f'{total_sum:.2f}');
#3, 5.51, 69.42, 100

