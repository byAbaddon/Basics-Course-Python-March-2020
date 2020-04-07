#journey
budget = float(input())
seaseon = input()
country = ''
place = ''


if budget <= 100:
    country = 'Bulgaria'
    if seaseon == 'summer':
        place = 'Camp'
        budget -= budget * 0.70
    else: 
        place = 'Hotel'
        budget -= budget * 0.30
  
elif budget > 100 and budget <= 1000:
      country = 'Balkans'
      if seaseon == 'summer':
        place = 'Camp'
        budget -= budget * 0.60
      else:
        place = 'Hotel'
        budget -= budget * 0.20
elif budget > 1000:
      country = 'Europe'
      place = 'Hotel'
      budget -= budget * 0.10

print(f'Somewhere in {country}\n{place} - {budget:.2f}');

#50, summer
#1500, summer