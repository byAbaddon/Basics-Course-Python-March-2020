n = float(input())
result = ''

if n <= 100:
    result = n + 5
elif n > 100 and n <= 1000:
    result = n * 1.20
elif  n > 1000:
    result = n * 1.10
  
if n % 2  == 0:
    result += 1 

if n % 10 == 5:
    result += 2 

points = abs(n - result)
print(f'{points}\n{result}');


# 2703

