#cinema
types =(input()) 
row = float(input())
col = float(input())
projectionType = {'Premiere' : 12.0, 'Normal' : 7.5, 'Discount' : 5.0 }
print(f'{(projectionType[types] * row * col):.2f} leva')

# Premiere, 10, 12
