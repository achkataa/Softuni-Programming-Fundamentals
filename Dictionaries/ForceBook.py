command = input()
my_dict = {}

def first_command_contains(users, my_user, side):
    for key, value in users.items():
        if my_user in value:
            return users
    if side in users:
        users[side].append(my_user)
        return users
    else:
        users[side] = [my_user]
        return users





def contains(users, my_user, side):
    for key, value in users.items():
        if my_user in value:
            value.remove(my_user)
            users[side].append(my_user)
            print(f"{my_user} joins the {side} side!")
            return users
    users[side].append(my_user)
    print(f"{my_user} joins the {side} side!")
    return users

def sorted_by_len(users):
    for k in sorted(users, key=lambda k: len(users[k]), reverse=True):
        return users


while command != "Lumpawaroo":
    if "|" in command:
        data = command.split(" | ")
        force_side = data[0]
        force_user = data[1]

        first_command_contains(my_dict, force_user, force_side)

    else:
        data = command.split(" -> ")
        force_user = data[0]
        force_side = data[1]

        contains(my_dict, force_user, force_side)

    command = input()



sorted_by_len = (my_dict)

for key, value in sorted(my_dict.items(), key=lambda x: x[0]):
    if len(my_dict[key]) == 0:
        del my_dict[key]
    else:
        print(f"Side: {key}, Members: {len(my_dict[key])}")
    for val in sorted(value):
        print(f"! {val}")




