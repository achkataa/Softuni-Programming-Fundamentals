our_money = float(input())
gender = input()
age = int(input())
sport = input()
card_price = 0

if gender == "m" and sport == "Gym":
    card_price = 42
elif gender == "m" and sport == "Boxing":
    card_price = 41
elif gender == "m" and sport == "Yoga":
    card_price = 45
elif gender == "m" and sport == "Zumba":
    card_price = 34
elif gender == "m" and sport == "Dances":
    card_price = 51
elif gender == "m" and sport == "Pilates":
    card_price = 39
elif gender == "f" and sport == "Gym":
    card_price = 35
elif gender == "f" and sport == "Boxing":
    card_price = 37
elif gender == "f" and sport == "Yoga":
    card_price = 42
elif gender == "f" and sport == "Zumba":
    card_price = 31
elif gender == "f" and sport == "Dances":
    card_price = 53
elif gender == "f" and sport == "Pilates":
    card_price = 37

if age <= 19:
    card_price = card_price - (card_price * 0.2)

if our_money >= card_price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${card_price - our_money:.2f} more.")






