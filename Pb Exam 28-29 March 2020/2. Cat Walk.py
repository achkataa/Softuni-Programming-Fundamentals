minutes = int(input())
walks = int(input())
calories = int(input())

total_walking_minutes = minutes * walks
burnt_calories = total_walking_minutes * 5
half_calories = calories * 0.5

if burnt_calories >= half_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burnt_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burnt_calories}.")