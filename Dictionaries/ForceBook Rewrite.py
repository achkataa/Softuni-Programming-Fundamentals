# command = input()
# my_dict = {}
#
# is_true = False
#
# while command != "Lumpawaroo":
#     if "|" in command:
#         data = command.split(" | ")
#         force_side = data[0]
#         force_user = data[1]
#
#         if force_side not in my_dict:
#             my_dict[force_side] = []
#
#         for key, value in my_dict.items():
#             if force_user in value:
#                 is_true = True
#
#         if is_true == False:
#             my_dict[force_side].append(force_user)
#
#
#     elif "->" in command:
#         data = command.split(" -> ")
#         force_user = data[0]
#         force_side = data[1]
#
#         if force_side not in my_dict:
#             my_dict[force_side] = []
#
#         old_side = ""
#
#         for key, value in my_dict.items():
#             if force_user in value:
#                 old_side = key
#                 is_true = True
#
#         if is_true == True:
#             my_dict[old_side].remove(force_user)
#             my_dict[force_side].append(force_user)
#         else:
#             my_dict[force_side].append(force_user)
#
#         print(f"{force_user} joins the {force_side} side!")
#
#
#
#
#     command = input()
#
#
# my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))
#
# for key, value in my_dict.items():
#     if len(value) == 0:
#         continue
#
#     print(f"Side: {key}, Members: {len(value)}")
#
#     for val in sorted(value):
#         print(f"! {val}")

command = input()
my_dict = {}

is_true = False

def add_user(users, side, currrent_user):
    is_true = False
    if side not in users:
        users[side] = []

    for key, value in users.items():
        if currrent_user in value:
            is_true = True

    if is_true == False:
        users[side].append(currrent_user)
    return users

def change_user_side(users, current_user, side):
    is_true = False
    if side not in users:
        users[side] = []

    old_side = ""

    for key, value in users.items():
        if current_user in value:
            old_side = key
            is_true = True

    if is_true == True:
        users[old_side].remove(current_user)
        users[side].append(current_user)
    else:
        users[side].append(current_user)

    return users




while command != "Lumpawaroo":
    if "|" in command:
        data = command.split(" | ")
        force_side = data[0]
        force_user = data[1]

        add_user(my_dict, force_side, force_user)


    elif "->" in command:
        data = command.split(" -> ")
        force_user = data[0]
        force_side = data[1]

        change_user_side(my_dict, force_user, force_side)

        print(f"{force_user} joins the {force_side} side!")




    command = input()


my_dict = dict(sorted(my_dict.items(), key=lambda x: (-len(x[1]), x[0])))

for key, value in my_dict.items():
    if len(value) == 0:
        continue

    print(f"Side: {key}, Members: {len(value)}")

    for val in sorted(value):
        print(f"! {val}")

