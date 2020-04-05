n = float(input())

if n <= 10:
    result = 'slow'
elif n > 10 and n <= 50:
    result = 'average'
elif n > 50 and n <= 150:
    result = 'fast'
elif n > 150 and n <= 1000:
    result = 'ultra fast'
elif n > 1000:
    result = 'extremely fast'
  
print(result)

# 49.5
