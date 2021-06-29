initial_energy = int(input())

command = input()

counter = 0
win_battles = 0

while command != "End of battle":
    distance = int(command)
    counter += 1

    if initial_energy >= distance:
        initial_energy -= distance
        win_battles += 1
    else:
        print(f"Not enough energy! Game ends with {win_battles} won battles and {initial_energy} energy")
        exit(0)

    if counter % 3 == 0:
        initial_energy += win_battles

    command = input()

print(f"Won battles: {win_battles}. Energy left: {initial_energy}")

