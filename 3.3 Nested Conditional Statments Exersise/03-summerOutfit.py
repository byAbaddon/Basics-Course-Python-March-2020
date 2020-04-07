# summerOutfit
degrees = int(input())
day_time = input()
result = 0
obj = { 
       'm': {'Morning':'Sweatshirt and Sneakers', 'Afternoon': 'Shirt and Moccasins',    'Evening': 'Shirt and Moccasins'},      
       'a': {'Morning':'Shirt and Moccasins',     'Afternoon': 'T-Shirt and Sandals',    'Evening': 'Shirt and Moccasins'},          
       'e': {'Morning':'T-Shirt and Sandals',     'Afternoon': 'Swim Suit and Barefoot', 'Evening': 'Shirt and Moccasins'},   
      }

if degrees >= 10 and degrees <= 18:
    if day_time == 'Morning':
        result = obj['m'][day_time]  
    elif day_time == 'Afternoon':
        result = obj['m'][day_time]
    else:
        result = obj['m'][day_time]  
elif degrees > 18 and degrees <= 24:
    if day_time == 'Morning':
        result = obj['a'][day_time]  
    elif day_time == 'Afternoon':
        result = obj['a'][day_time]
    else:
        result = obj['a'][day_time]       
elif degrees >= 25:
    if day_time == 'Morning':
        result = obj['e'][day_time]  
    elif day_time == 'Afternoon':
        result = obj['e'][day_time]
    else:
        result = obj['e'][day_time]

print(f"It's {degrees} degrees, get your {result}.")

# 16, Morning
# 16, Afternoon
# 22, Afternoon
# 28, Evening
