treasure_chest = input().split("|")

command = input()


def loot(list, items):
    for item in items:
        if item not in list:
            list.insert(0, item)


def drop(list, index):
    if -1 < index < len(list):
        item = list.pop(index)
        list.append(item)


def steal(list, count):
    removed_items = []
    for i in range(count):
        if list:
            removed_items.append(list.pop())
    print(', '.join(reversed(removed_items)))


while command != "Yohoho!":
    data = command.split()
    action = data[0]

    if action == "Loot":
        items = data[1:]
        loot(treasure_chest, items)
    elif action == "Drop":
        index = int(data[1])
        drop(treasure_chest, index)
    elif action == "Steal":
        count = int(data[1])
        steal(treasure_chest, count)

    command = input()


def sum_of_chars(list):
    the_sum = 0
    for item in list:
        the_sum += len(item)
    return the_sum



if not treasure_chest:
    print("Failed treasure hunt.")
else:
    print(f"Average treasure gain: {sum_of_chars(treasure_chest) / len(treasure_chest):.2f} pirate credits.")