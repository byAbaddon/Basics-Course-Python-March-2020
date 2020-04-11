#sumNumbers
sum_num = 0

while True:
    num = input()
    if num == 'Stop':
        print(sum_num)
        break
    sum_num += int(num)

#10 , 20, 30, 45, Stop
