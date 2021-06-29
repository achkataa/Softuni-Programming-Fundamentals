initial_inventory = [item for item in input().split(", ")]

command = input()

def collect(inventory, item):
    if item not in inventory:
        inventory.append(item)
    return inventory

def drop(inventory, item):
    if item in inventory:
        inventory.remove(item)
    return inventory

def combine(inventory, old_item, new_item):
    if old_item in inventory:
        old_item_index = inventory.index(old_item)
        inventory.insert(old_item_index + 1, new_item)
    return inventory

def renew(inventory, item):
    if item in inventory:
        inventory.remove(item)
        inventory.append(item)

while command != "Craft!":
    data = command.split(" - ")
    action = data[0]

    if action == "Collect":
        item = data[1]
        collect(initial_inventory, item)
    elif action == "Drop":
        item = data[1]
        drop(initial_inventory, item)
    elif action == "Combine Items":
        old_item, new_item = data[1].split(":")
        combine(initial_inventory, old_item, new_item)
    elif action == "Renew":
        item = data[1]
        renew(initial_inventory, item)

    command = input()


print(', '.join(initial_inventory))