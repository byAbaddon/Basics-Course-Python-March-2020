day =  float(input())
man =  float(input())
tort = float(input()) * 45
gorf = float(input()) * 5.80
pan_cake = float(input()) * 3.20

sum = (tort + gorf + pan_cake) * man
totalSum = (sum * day) * 0.875
print(f'{totalSum:.2f}')

