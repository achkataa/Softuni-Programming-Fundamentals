shopping_list = [product for product in input().split("!")]

command = input()


def urgent(list, item):
    if not item in list:
        list.insert(0, item)

def unnecessary(list, item):
    if item in list:
        list.remove(item)

def correct(list, old_item, new_item):
    if old_item in list:
        old_item_index = list.index(old_item)
        list[old_item_index] = new_item

def rearrange(list, item):
    if item in list:
        list.remove(item)
        list.append(item)


while command != "Go Shopping!":
    data = command.split()
    action = data[0]

    if action == "Urgent":
        item = data[1]
        urgent(shopping_list, item)
    elif action == "Unnecessary":
        item = data[1]
        unnecessary(shopping_list, item)
    elif action == "Correct":
        old_item = data[1]
        new_item = data[2]
        correct(shopping_list, old_item, new_item)
    elif action == "Rearrange":
        item = data[1]
        rearrange(shopping_list, item)

    command = input()

print(', '.join(shopping_list))