targets = [int(target) for target in input().split()]

command = input()

def valid_index(list, index):
    if 0 <= index < len(list):
        return True
    return False

def shoot(list, index, power):
    list[index] -= power
    return list

def add(list, index, value):
    list.insert(index, value)
    return list

def strike(list, radius_l, radius_r,):
    del list[radius_l:radius_r+1]
    return list

while command != "End":
    data = command.split()
    action = data[0]

    if action == "Shoot":
        index = int(data[1])
        power = int(data[2])
        if valid_index(targets, index):
            shoot(targets, index, power)
            if targets[index] <= 0:
                targets.remove(targets[index])

    elif action == "Add":
        index = int(data[1])
        value = int(data[2])
        if valid_index(targets, index):
            add(targets, index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(data[1])
        radius = int(data[2])
        if valid_index(targets, index):
            radius_right = index + radius
            radius_left = index - radius
            if radius_left >= 0 and radius_right < len(targets):
                strike(targets, radius_left, radius_right)
            else:
                print("Strike missed!")
        else:
            print("Strike missed!")
    command = input()

print('|'.join(str(target) for target in targets))