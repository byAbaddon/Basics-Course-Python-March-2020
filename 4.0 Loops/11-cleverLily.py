#cleverLily
age = int(input())
laundry_price = float(input())
toys_price = int(input())
money_count = 0
toys_count = 0
brother_reket = 0

for i in range(1, age + 1):
    if i % 2 == 0:
        money_count += (10 * i)
        brother_reket += 1
    else:
         toys_count += 1
   
toys_count *= toys_price
subtotal = (toys_count + (money_count / 2)) - brother_reket
total = abs(subtotal - laundry_price)

if subtotal >= laundry_price:
      print(f'Yes! {total:.2f}')
else:
      print(f'No! {total:.2f}')

#10, 170, 6