health = 100
bitcoins = 0

rooms = [room for room in input().split("|")]

for room in rooms:
    data = room.split(" ")
    command = data[0]
    number = int(data[1])

    if command == "potion":
        if health + number > 100:
            print(f"You healed for {100 - health} hp.")
            print(f"Current health: {100} hp.")
            health += 100 - health
        else:
            health += number
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:

        health -= number

        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms.index(room) + 1}")
            exit(0)

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")



