# tradeCommissions
import sys 

city = input()
money = float(input())
arr = ["Sofia", "Varna", "Plovdiv"];
result = 0;

obj = {
    'Sofia': { 's': 5, 'm': 7, 'l': 8, 'xl': 12 }, 
    'Varna': { 's': 4.5, 'm': 7.5, 'l': 10, 'xl': 13 }, 
    'Plovdiv': { 's': 5.5, 'm': 8, 'l': 12, 'xl': 14.5 }
  }

if (city in arr) == False or (money < 0) == True:
    print("error");
    sys.exit()

if money <= 500:
    result = (obj[city]['s'] * money) / 100
elif money > 500 and money <= 1000:
    result = (obj[city]['m'] * money) / 100
elif money > 1000 and money <= 10000:
   result = (obj[city]['l'] * money) / 100
elif money > 10000:
   result = (obj[city]['xl'] * money) / 100

print(f'{result:.2f}')

# Varna
# 3874.50
