turns = int(input())
points = 0
first_option = 0
second_option = 0
third_option = 0
fourth_option = 0
fifth_option = 0
sixth_option = 0
for turn in range(1, turns + 1):
    number = int(input())
    if number >= 0 and number <= 9:
        first_option += 1
        points = points + (0.2 * number)
    elif number >= 10 and number <= 19:
        second_option += 1
        points = points + (0.3 * number)
    elif number >= 20 and number <= 29:
        third_option += 1
        points = points + (0.4 * number)
    elif number >= 30 and number <=39:
        fourth_option += 1
        points = points + 50
    elif number >= 40 and number <= 50:
        fifth_option += 1
        points = points + 100
    elif number > 50 or number < 0:
        sixth_option += 1
        points = points / 2

print(f"{points:.2f}")
print(f"From 0 to 9: {first_option * 100 / turns:.2f}%")
print(f"From 10 to 19: {second_option * 100 / turns:.2f}%")
print(f"From 20 to 29: {third_option * 100 / turns:.2f}%")
print(f"From 30 to 39: {fourth_option * 100 / turns:.2f}%")
print(f"From 40 to 50: {fifth_option * 100 / turns:.2f}%")
print(f"Invalid numbers: {sixth_option * 100 / turns:.2f}%")

