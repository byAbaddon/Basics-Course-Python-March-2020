#skiTrip
days = int(input()) -1
room = input()
grade = input()
result = 0;
price_per_night = {"room for one person": 18.00, "apartment" : 25.00, "president apartment": 35.00};

if days < 10:
    if room == 'room for one person':
        result = days * price_per_night[room]; 
    elif room == 'apartment':
        result = days * price_per_night[room]
        result-= result * 30 / 100
    else:
        result = days * price_per_night[room]
        result-= result * 10 / 100
elif days >= 10 and days <= 15:
    if room == 'room for one person':
        result = days * price_per_night[room]; 
    elif room == 'apartment':
        result = days * price_per_night[room]
        result-= result * 35 / 100
    else:
        result = days * price_per_night[room]
        result-= result * 15 / 100
elif days > 15:
    if room == 'room for one person':
            result = days * price_per_night[room]; 
    elif room == 'apartment':
         result = days * price_per_night[room]
         result-= result * 50 / 100
    else:
        result = days * price_per_night[room]
        result-= result * 20 / 100
        
print(f'{result * 125 / 100:.2f}'  if grade == 'positive' else f'{result * 0.90:.2f}')

#skiTrip "30", "president apartment", "negative" 

