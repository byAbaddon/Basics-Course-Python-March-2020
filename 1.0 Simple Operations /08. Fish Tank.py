long =  int(input())
short = int(input())
hight = int(input())
precent = float(input())

size = long * short * hight * 0.001
calc_precent =  precent * 0.01
sum = (size  * (1 - calc_precent))
print(f'{sum:.3f}')

 
