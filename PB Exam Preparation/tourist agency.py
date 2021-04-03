city = input()
packet = input()
vip = input()
days = int(input())

price = 0
dscount = 0


if city == "Bansko" and packet == "noEquipment":
    price = 80
    if vip == "yes":
        price = price - (price * 0.05)
if city == "Bansko" and packet == "withEquipment":
    price = 100
    if vip == "yes":
        price = price - (price * 0.1)
if city == "Borovets" and packet == "noEquipment":
    price = 80
    if vip == "yes":
        price = price - (price * 0.05)
if city == "Borovets" and packet == "withEquipment":
    price = 100
    if vip == "yes":
        price = price - (price * 0.1)
if city == "Varna" and packet == "noBreakfast":
    price = 100
    if vip == "yes":
        price = price - (price * 0.07)
if city == "Varna" and packet == "withBreakfast":
    price = 130
    if vip == "yes":
        price = price - (price * 0.12)
if city == "Burgas" and packet == "noBreakfast":
    price = 100
    if vip == "yes":
        price = price - (price * 0.07)
if city == "Burgas" and packet == "withBreakfast":
    price = 130
    if vip == "yes":
        price = price - (price * 0.12)


total = price * days



if days > 7:
    total -= price
if days < 1:
    print("Days must be positive number!")
elif city != "Bansko" and city != "Borovets" and city !=  "Varna" and city != "Burgas" and packet != "yes" and packet != "no":
    print("Invalid input!")
else:
    print(f"The price is {total:.2f}lv! Have a nice time!")



