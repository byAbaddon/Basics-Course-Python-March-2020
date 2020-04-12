#traveling
destination = input()

while destination != 'End':
    budget = float(input())
    money = 0

    while budget > money:
        tips = float(input())
        money += tips

    print(f'Going to {destination}!')

    destination = input()

   
#'Greece', '1000', '200', '200', '300', '100', '150', '240', 'Spain', '1200', '300', '500', '193', '423', 'End'
'''  --------------------------------------- 90pts   TODO
destination_dict = {}      

while True:
   current = input()

   if current == 'End':
      break
   elif len(current) > 4:
      destination_dict[current] = int(input())
      key = current
   else:   
      destination_dict[key] -= int(current)
     
for county, budget in destination_dict.items():
    if budget <= 0 :
        print(f'Going to {county}!')
'''