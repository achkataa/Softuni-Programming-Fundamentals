command = input()
sum = 0
total_price = 0

while command != 'special' and command != 'regular':
    command = float(command)

    if command < 0:
        print("Invalid price!")
    else:
        sum += command
    command = input()

if sum == 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum:.2f}$")
    taxes = sum * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    total = sum + taxes
    if command == "special":
        total -= total * 0.1
    print(f"Total price: {total:.2f}$")







