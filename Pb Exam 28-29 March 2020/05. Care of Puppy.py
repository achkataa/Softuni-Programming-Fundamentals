bought_food = int(input())
bought_food_in_grams = bought_food * 1000
total_eaten_food = 0
command = input()
while command != "Adopted":
    eaten_food_daily = int(command)
    total_eaten_food += eaten_food_daily
    command = input()
if total_eaten_food <= bought_food_in_grams:
    print(f"Food is enough! Leftovers: {bought_food_in_grams - total_eaten_food} grams.")
else:
    print(f"Food is not enough. You need {abs(bought_food_in_grams - total_eaten_food)} grams more.")




