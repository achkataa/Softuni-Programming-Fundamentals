wanted_income = float(input())
price = 0
total = 0
command = input()

while command != "Party!":
    number_beverages = int(input())

    price = len(command) * number_beverages

    if price % 2 != 0:
        price = price - (price * 0.25)

    total += price

    if total >= wanted_income:
        print("Target acquired.")
        break

    price = 0
    command = input()


else:
    if total < wanted_income:
        print(f"We need {wanted_income - total:.2f} leva more.")
    else:
        print(f"Target acquired.")

print(f"Club income - {total:.2f} leva.")

