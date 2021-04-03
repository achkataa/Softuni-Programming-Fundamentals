journal = [item for item in input().split(", ")]

command = input()

while command != "Craft!":
    data = command.split(" - ")
    task = data[0]
    material = data[1]

    if task == "Collect":
        if not material in journal:
            journal.append(material)

    if task == "Drop":
        if material in journal:
            journal.remove(material)

    if task == "Combine Items":
        data = material.split(":")
        old_item = data[0]
        new_item = data[1]

        if old_item in journal:
            index = journal.index(old_item)
            journal.insert(index + 1, new_item)

    if task == "Renew":
        if material in journal:
            journal.remove(material)
            journal.append(material)

    command = input()

print(", ".join(journal))