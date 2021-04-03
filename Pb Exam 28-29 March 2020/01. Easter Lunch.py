cake_count = int(input())
eggs_count = int(input())
biscuits_count = int(input())

cake_price = cake_count * 3.20
eggs_price = eggs_count * 4.35
biscuits_price = biscuits_count * 5.40
eggs_paint = (eggs_count * 12) * 0.15

total_price = cake_price + eggs_price + biscuits_price + eggs_paint

print(f"{total_price:.2f}")