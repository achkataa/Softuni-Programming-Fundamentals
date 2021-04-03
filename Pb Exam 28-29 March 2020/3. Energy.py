fruit = input()
size = input()
number_ordered_sets = int(input())
price = 0
discount = 0

if fruit == "Watermelon" and size == "small":
    price = 56 * 2
    total_price = price * number_ordered_sets
elif fruit == "Watermelon" and size == "big":
    price = 28.70 * 5
    total_price = price * number_ordered_sets
elif fruit == "Mango" and size == "small":
    price = 36.66 * 2
    total_price = price * number_ordered_sets
elif fruit == "Mango" and size == "big":
    price = 19.60 * 5
    total_price = price * number_ordered_sets
elif fruit == "Pineapple" and size == "small":
    price = 42.10 * 2
    total_price = price * number_ordered_sets
elif fruit == "Pineapple" and size == "big":
    price = 24.80 * 5
    total_price = price * number_ordered_sets
elif fruit == "Raspberry" and size == "small":
    price = 20 * 2
    total_price = price * number_ordered_sets
elif fruit == "Raspberry" and size == "big":
    price = 15.20 * 5
    total_price = price * number_ordered_sets

if total_price >= 400 and total_price <= 1000:
    discount = total_price * 0.15
    total_price = total_price - discount
elif total_price > 1000:
    discount = total_price * 0.5
    total_price = total_price - discount


print(f"{total_price:.2f} lv.")

