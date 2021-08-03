

#   FIRST SOLUTION

pirate_ship = [int(num) for num in input().split(">")]
warship = [int(num) for num in input().split(">")]
max_health = int(input())

command = input()


def fire(warship, index, damage):
    if -1 < index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0:
            return True

def defend(pirate_ship, start_index, end_index, damage):
    if -1 < start_index < len(pirate_ship) and -1 < end_index < len(pirate_ship):
        for i in range(start_index, end_index + 1):
            pirate_ship[i] -= damage
            if pirate_ship[i] <= 0:
                return True

def repair(pirate_ship, index, health):
    if -1 < index < len(pirate_ship):
        if pirate_ship[index] + health > max_health:
            pirate_ship[index] = max_health
        else:
            pirate_ship[index] += health




def status(pirate_ship):
    repair_border = max_health * 0.2
    counter = 0
    for num in pirate_ship:
        if num < repair_border:
            counter += 1
    return counter

while command != "Retire":
    data = command.split()
    action = data[0]

    if action == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if fire(warship, index, damage):
            print("You won! The enemy ship has sunken.")
            exit(0)
    elif action == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if defend(pirate_ship, start_index, end_index, damage):
            print("You lost! The pirate ship has sunken.")
            exit(0)

    elif action == "Repair":
        index = int(data[1])
        health = int(data[2])
        repair(pirate_ship, index, health)

    elif action == "Status":
        print(f"{status(pirate_ship)} sections need repair.")

    command = input()

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")



# SECOND SOLUTION


# pirate_ship = [int(num) for num in input().split(">")]
# warship = [int(num) for num in input().split(">")]
# max_health = int(input())
#
# command = input()
#
# while command != "Retire":
#     data = command.split()
#     action = data[0]
#
#     if action == "Fire":
#         index = int(data[1])
#         damage = int(data[2])
#
#         if 0 <= index < len(warship):
#             warship[index] -= damage
#             if warship[index] <= 0:
#                 print("You won! The enemy ship has sunken.")
#                 exit(0)
#     elif action == "Defend":
#         start_index = int(data[1])
#         end_index = int(data[2])
#         damage = int(data[3])
#
#         if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
#             for index in range(start_index, end_index + 1):
#                 pirate_ship[index] -= damage
#                 if pirate_ship[index] <= 0:
#                     print("You lost! The pirate ship has sunken.")
#                     exit(0)
#     elif action == "Repair":
#         index = int(data[1])
#         health = int(data[2])
#
#         if 0 <= index < len(pirate_ship):
#             if pirate_ship[index] + health > max_health:
#                 pirate_ship[index] = max_health
#             else:
#                 pirate_ship[index] += health
#
#
#     elif action == "Status":
#         threshold = max_health * 0.2
#         print(f"{len([num for num in pirate_ship if num < threshold])} sections need repair.")
#
#     command = input()
#
# print(f"Pirate ship status: {sum(pirate_ship)}")
# print(f"Warship status: {sum(warship)}")


