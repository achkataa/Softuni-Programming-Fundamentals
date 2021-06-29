rooms = [room for room in input().split("|")]

initial_health = 100
initial_bitcoin = 0

for room in rooms:
    data = room.split()
    command = data[0]
    number = int(data[1])

    if command == "potion":
        if initial_health + number > 100:
            print(f"You healed for {100 - initial_health} hp.")
            print(f"Current health: {100} hp.")
            initial_health += 100 - initial_health
        else:
            initial_health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {initial_health} hp.")
    elif command == "chest":
        initial_bitcoin += number
        print(f"You found {number} bitcoins.")

    else:
        initial_health -= number
        if initial_health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            exit(0)

print("You've made it!")
print(f"Bitcoins: {initial_bitcoin}")
print(f"Health: {initial_health}")