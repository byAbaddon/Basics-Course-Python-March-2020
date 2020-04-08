#leftAndRightSum
loop =  int(input()) * 2
list_num = []

while loop > 0 :
    list_num.append(int(input()))
    loop -= 1

left_sum = sum(list_num[: len(list_num) // 2])
right_sum  = sum(list_num[len(list_num) // 2 :])
result = left_sum - right_sum

if result != 0:
    print(f'No, diff = {abs(result)}') 
else:
    print(f'Yes, sum = {left_sum}')

#2, 10, 90, 60, 40 

