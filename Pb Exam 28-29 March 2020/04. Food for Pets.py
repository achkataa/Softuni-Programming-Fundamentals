days = int(input())
food_amount = float(input())
day_food = 0
biscuit = 0
dog_food = 0
cat_food = 0
eaten_food = 0
for day in range(1, days + 1):
    food_ate_by_dog = int(input())
    food_ate_by_cat = int(input())
    if day % 3 == 0:
        dog_food += food_ate_by_dog
        cat_food += food_ate_by_cat
        eaten_food = dog_food + cat_food
        day_food = food_ate_by_dog + food_ate_by_cat
        biscuit = day_food * 0.1
    else:
        dog_food += food_ate_by_dog
        cat_food += food_ate_by_cat
        eaten_food = dog_food + cat_food

print(f"Total eaten biscuits: {round(biscuit)}gr.")
print(f"{(eaten_food / food_amount) * 100:.2f}% of the food has been eaten.")
print(f"{(dog_food / eaten_food) * 100:.2f}% eaten from the dog.")
print(f"{(cat_food / eaten_food) * 100:.2f}% eaten from the cat.")

