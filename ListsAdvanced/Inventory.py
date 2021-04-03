initial_items = [item for item in input().split(", ")]
command = input()

def collect(i):
    if not i in initial_items:
        return initial_items.append(i)

def drop(i):
    if i in initial_items:
        return initial_items.remove(i)

def combine_itmes(i):
    split_items = i.split(":")
    old_item = split_items[0]
    new_item = split_items[1]
    if old_item in initial_items:
        index = initial_items.index(old_item)
        return initial_items.insert(index + 1, new_item)

def renew(i):
    if i in initial_items:
        return initial_items.append(initial_items.pop(initial_items.index(i)))

while command != "Craft!":
    data = command.split(" - ")

    task = data[0]
    item = data[1]

    if task == "Collect":
        collect(item)
    elif task == "Drop":
        drop(item)
    elif task == "Combine Items":
        combine_itmes(item)
    elif task == "Renew":
        renew(item)
    command = input()

print(", ".join(initial_items))






