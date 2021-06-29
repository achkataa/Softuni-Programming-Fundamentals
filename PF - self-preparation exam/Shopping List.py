# initial_shopping_list = input().split("!")
#
# command = input()
#
#
# def urgent(list, product):
#     if product not in list:
#         list.insert(0, product)
#
# def unnecessary(list, product):
#     if product in list:
#         list.remove(product)
#
# def correct(list, old_product, new_product):
#     if old_product in list:
#         index = list.index(old_product)
#         list[index] = new_product
#
# def rearrange(list, product):
#     if product in list:
#         list.remove(product)
#         list.append(product)
#
#
# while command != "Go Shopping!":
#     data = command.split()
#     action = data[0]
#
#     if action == "Urgent":
#         item = data[1]
#         urgent(initial_shopping_list, item)
#     elif action == "Unnecessary":
#         item = data[1]
#         unnecessary(initial_shopping_list, item)
#     elif action == "Correct":
#         old_item = data[1]
#         new_item = data[2]
#         correct(initial_shopping_list, old_item, new_item)
#     elif action == "Rearrange":
#         item = data[1]
#         rearrange(initial_shopping_list, item)
#
#     command = input()
#
# print(', '.join(initial_shopping_list))
#
#


initial_shopping_list = input().split("!")

command = input()

def urgent(list, *args):
    if args[0] not in list:
        list.insert(0, args[0])

def unnecessary(list, *args):
    if args[0] in list:
        list.remove(args[0])

def correct(list, *args):
    if args[0] in list:
        index = list.index(args[0])
        list[index] = args[1]

def rearrange(list, *args):
    if args[0] in list:
        list.remove(args[0])
        list.append(args[0])


mapper = {
    "Urgent": urgent,
    "Unnecessary": unnecessary,
    "Correct": correct,
    "Rearrange": rearrange
}


while command != "Go Shopping!":
    data = command.split()
    action = data[0]
    rest = data[1:]

    mapper[action](initial_shopping_list, *rest)

    command = input()

print(', '.join(item for item in initial_shopping_list))



