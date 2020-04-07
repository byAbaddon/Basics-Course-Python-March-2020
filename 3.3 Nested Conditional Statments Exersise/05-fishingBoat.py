#fishingBoat
budget = int(input())
season = input()
fishermen = int(input())

seasonPrice = {'Spring': 3000, 'Summer': 4200, 'Autumn': 4200, 'Winter': 2600};
result = seasonPrice[season];

if fishermen <= 6:
    result-= result * 0.1;
elif fishermen >= 7 and fishermen <= 11:
    result-= result * 0.15;
elif fishermen > 12:
    result -= result * 0.25;

if season != "Autumn" and (fishermen & 1) == 0:
    result -= result * 0.05;
  
total = abs(budget - result)

if result > budget:
    print(f'Not enough money! You need {total:.2f} leva.')  
else: 
    print(f'Yes! You have {total:.2f} leva left.')
    
#3000, Summer, 11

