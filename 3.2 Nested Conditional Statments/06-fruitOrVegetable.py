#fruitOrVegetable
search = input()
collections = ["bannana","banana", "apple", "kiwi", "cherry", "lemon", "grapes", "tomato","cucumber", "pepper", "carrot" ];
  
if search in collections:
    print( "fruit" if collections.index(search) <= 6 else "vegetable")
else:
    print("unknown")
  
#JUDGE BUG  - bannana
#banana
#bannana


