months = int(input())
total_expenses = 0
total_electricity = 0
total_internet = 0
total_water = 0
other_expenses = 0
final_bill = 0
water_price = 0
internet_price = 0

for month in range(1, months + 1):
    electicity = float(input())
    water_price = 20
    internet_price = 15
    total_electricity += electicity
    total_water += 20
    total_internet += 15
    total_expenses = electicity + water_price + internet_price
    other_expenses = other_expenses + ((total_expenses) + (total_expenses * 0.2))
    final_bill = (total_electricity + total_water + total_internet + other_expenses) / months

print(f"Electricity: {total_electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {other_expenses:.2f} lv")
print(f"Average: {final_bill:.2f} lv")


