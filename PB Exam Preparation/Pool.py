import math

people = int(input())
fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())


total_fee = people * fee
deck_chairs_needed = math.ceil(people * 0.75)
deck_chairs_total = deck_chairs_needed * deck_chair_price
umbrella_need = math.ceil(people / 2)
umbrella_total = umbrella_need * umbrella_price

total = total_fee + deck_chairs_total + umbrella_total

print(f"{total:.2f} lv.")

