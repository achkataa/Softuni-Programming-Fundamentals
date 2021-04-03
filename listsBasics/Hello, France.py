products_and_prices = input().split("|")
budget = float(input())
new_prices = []
old_prices_total = 0
new_prices_total = 0
total_prices = []

for product_and_price in products_and_prices:
    product, price = product_and_price.split("->")
    int_price = float(price)

    if product == "Clothes":
        if int_price > 50.00:
            continue
    if product == "Shoes":
        if int_price > 35.00:
            continue
    if product == "Accessories":
        if int_price > 20.50:
            continue
    if int_price > budget:
        continue
    else:
        old_prices_total += int_price
        new_prices.append(int_price)
        budget = budget - int_price

for element in new_prices:
    element = element + (element * 0.40)
    total_prices.append(f"{element:.2f}")
    new_prices_total += element



print(*total_prices, sep=" ")
print(f"Profit: {new_prices_total - old_prices_total:.2f}")

if new_prices_total + budget >= 150:
    print("Hello, France!")
else:
    print("Time to go.")

