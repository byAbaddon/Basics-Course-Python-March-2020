count_table = float(input())
length  = float(input())
wide = float(input())

calcOne = count_table * (length + 2 * 0.30) * (wide + 2 * 0.30) 
calcTwo = count_table * (length  / 2 ) * (length / 2)
dolars = (calcOne * 7 + calcTwo * 9)
to_lv = (dolars * 1.85)
print(f'{dolars:.2f} USD\n{to_lv:.2f} BGN')


''' input:
 5
1.00
0.50

''' 
