#animalType
animal = input()
result = ''
listReptile = ["snake", "tortoise", "crocodile"]

if animal == 'dog':
    result = 'mammal'
elif animal in listReptile:
    result = 'reptile'
else:  
    result = 'unknown'

print(result)    

# dog
# snake

