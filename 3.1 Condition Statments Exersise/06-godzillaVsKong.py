#Godzilla
budget = float(input())
statitst = float(input())
clothes = float(input())

decors = budget / 10
clothes_sum = statitst * clothes

if statitst > 150:
    clothes_sum -= (clothes_sum / 10)
      
budget-= (decors + clothes_sum)

if budget >= 0:
    print(f'Action!\nWingard starts filming with {budget:.2f} leva left.')
else:
  print(f'Not enough money!\nWingard needs {abs(budget):.2f} leva more.')


# 20000, 120, 55.5
# 9587.88, 222, 55.68
