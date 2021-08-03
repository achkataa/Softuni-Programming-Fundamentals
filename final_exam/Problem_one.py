needed_experience = float(input())
count_of_battles = int(input())


current_experience = 0
battle = 0

for i in range(1, count_of_battles + 1):
    experience_per_battle = float(input())

    if i % 3 == 0:
        current_experience += experience_per_battle + (experience_per_battle * 0.15)

    elif i % 5 == 0:
        current_experience += experience_per_battle - (experience_per_battle * 0.10)

    elif i % 15 == 0:
        current_experience += experience_per_battle + (experience_per_battle * 0.5)
    else:
        current_experience += experience_per_battle

    if current_experience >= needed_experience:
        battle = i
        break


if current_experience >= needed_experience:
    print(f"Player successfully collected his needed experience for {battle} battles.")
else:
    print(f"Player was not able to collect the needed experience, {needed_experience - current_experience:.2f} more needed.")

