whiskey_leva = float(input())
beerLt = float(input())
wineLt = float(input()) 
racia_lt = float(input()) 
whiskey_lt = float(input()) 

priceLt_rakia =  whiskey_leva  / 2
priceLt_wine = priceLt_rakia * 0.60 
priceLt_beer =  priceLt_rakia   * 0.20
all_sum = (racia_lt * priceLt_rakia) + (wineLt * priceLt_wine) + (beerLt * priceLt_beer) +(whiskey_lt *  whiskey_leva)

print(f'{all_sum:.2f}')


