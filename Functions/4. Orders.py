input_product = input()
input_quantity = int(input())


def oreders_total_price(product, number):
    if product == "coffee":
        total_price = f"{number * 1.50:.2f}"
    elif product == "water":
        total_price = f"{number * 1.00:.2f}"
    elif product == "coke":
        total_price = f"{number * 1.40:.2f}"
    elif product == "snacks":
        total_price = f"{number * 2.00:.2f}"

    return total_price

print(oreders_total_price(input_product, input_quantity))