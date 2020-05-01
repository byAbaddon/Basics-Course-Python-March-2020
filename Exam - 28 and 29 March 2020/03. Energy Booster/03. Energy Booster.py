booster = {
  "small" : { "Watermelon" : 56.00 , "Mango" : 36.66, "Pineapple" : 42.10 , "Raspberry" : 20.00},
  "big" : { "Watermelon" : 28.70 , "Mango" : 19.60, "Pineapple" : 24.80 , "Raspberry" : 15.20},
}

kind = input()
size = input()
count = int(input())
add = 0

if size == 'small':
   add = 2
else:
   add = 5
   
packet = booster[size][kind] * add * count

if packet >= 400 and packet <= 1000:
  packet = packet * 0.85
elif packet > 1000:
  packet = packet * 0.50
else:
  packet  
  
print(f'{packet:.2f} lv.') 