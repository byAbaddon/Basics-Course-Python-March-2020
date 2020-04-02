#toyShop
trip = float(input())
puzzle = float(input())
doll = float(input())
bear = float(input())
minion = float(input())
truck = float(input())
numbers = puzzle + doll + bear + minion + truck;
toy_price = (puzzle * 2.60) + (doll * 3) + (bear * 4.1) + (minion * 8.20) + (truck * 2);

if numbers >= 50:
    price = toy_price * 0.75;
    total_price = price * 0.90;
    if total_price >= trip:
         print(f'Yes! {(total_price - trip):.2f} lv left.')
    else:        
        print(f'Not enough money! {(trip - total_price):.2f} lv needed.')
if numbers < 50:
    total_price = toy_price * 0.90;
    if total_price >= trip:
        print(f'Yes! {(total_price - trip):.2f} lv left.')
    else:
        print(f'Not enough money! {(trip - total_price):.2f} lv needed.')

'''
320
8
2
5
5
1
output: Not enough money! 238.73 lv needed.
'''