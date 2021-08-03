command = input()

total_price_without_tax = 0
taxes = 0
total_price = 0

while command != "special" and command != "regular":
    part_price = float(command)
    if part_price > -1:
        total_price_without_tax += part_price
        taxes += part_price * 0.2
    else:
        print("Invalid price!")
    command = input()


def print_results(total_price_without_tax, taxes, total_price):
    if total_price > 0:
        print("Congratulations you've just bought a new computer!")
        print(f"Price without taxes: {total_price_without_tax:.2f}$")
        print(f"Taxes: {taxes:.2f}$")
        print("-----------")
        print(f"Total price: {total_price:.2f}$")
    else:
        print("Invalid order!")


if command == "special":
    total_price = (total_price_without_tax + taxes) - ((total_price_without_tax + taxes) * 0.1)
    print_results(total_price_without_tax, taxes, total_price)

else:
    total_price = total_price_without_tax + taxes
    print_results(total_price_without_tax, taxes, total_price)


