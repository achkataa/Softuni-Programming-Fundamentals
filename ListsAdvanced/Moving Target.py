targets = input().split()

targets_list = [int(target) for target in targets]

command = input()

while command != "End":
    command = command.split()
    token = command[0]
    index = 0
    value = 0

    if token == "Shoot":

        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets_list):
            targets_list[index] -= value
            if targets_list[index] <= 0:
                targets_list.pop(index)

    elif token == "Add":
        index = int(command[1])
        value = int(command[2])
        if 0 <= index < len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")

    elif token == "Strike":
        index = int(command[1])
        radius = int(command[2])
        start = index - radius
        end = index + radius

        if start >= 0 and end < len(targets_list):
            del targets_list[start: end + 1]
        else:
            print("Strike missed!")

    command = input()

targets_list = [str(task) for task in targets_list]
print("|".join(targets_list))


