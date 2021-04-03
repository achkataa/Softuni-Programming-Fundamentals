price_skumriq = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())

palamud_price = price_skumriq + (price_skumriq * 0.60)
sum_palamud = kg_palamud * palamud_price

safrid_price = price_caca + (price_caca * 0.80)
sum_safrid = kg_safrid * safrid_price

sum_midi = 7.50 * kg_midi

total = sum_palamud + sum_safrid + sum_midi
print(round(total,2))