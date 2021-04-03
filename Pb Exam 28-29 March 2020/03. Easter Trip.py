destination = input()
dates = input()
nights = int(input())
price_for_night = 0

if destination == "France" and dates == "21-23":
    price_for_night = 30
elif destination == "France" and dates == "24-27":
    price_for_night = 35
elif destination == "France" and dates == "28-31":
    price_for_night = 40
elif destination == "Italy" and dates == "21-23":
    price_for_night = 28
elif destination == "Italy" and dates == "24-27":
    price_for_night = 32
elif destination == "Italy" and dates == "28-31":
    price_for_night = 39
elif destination == "Germany" and dates == "21-23":
    price_for_night = 32
elif destination == "Germany" and dates == "24-27":
    price_for_night = 37
elif destination == "Germany" and dates == "28-31":
    price_for_night = 43

total_money = nights * price_for_night

print(f"Easter trip to {destination} : {total_money:.2f} leva.")



