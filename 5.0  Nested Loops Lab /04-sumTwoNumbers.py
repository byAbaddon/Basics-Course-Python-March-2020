#sumTwoNumbers
import sys
first, second, magic_num = int(input()), int(input()), int(input())
counter = 0

for i in range(first,second + 1):
    for j in range(first, second + 1):
        counter += 1
        if magic_num == i + j:
            print(f'Combination N:{counter} ({i} + {j} = {magic_num})')
            sys.exit()

print(f'{counter} combinations - neither equals {magic_num}');

# 1, 10, 5

