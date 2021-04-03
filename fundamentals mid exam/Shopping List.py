grocery = [item for item in input().split("!")]

command = input()

while command != "Go Shopping!":
    data = command.split()
    command_kind = data[0]

    if command_kind == "Urgent":
        if not data[1] in grocery:
            grocery.insert(0, data[1])
    elif command_kind == "Unnecessary":
        if data[1] in grocery:
            grocery.remove(data[1])
    elif command_kind == "Correct":
        if data[1] in grocery:
            index = grocery.index(data[1])
            grocery[index] = data[2]
    elif command_kind == "Rearrange":
        if data[1] in grocery:
            grocery.remove(data[1])
            grocery.append(data[1])

    command = input()


print(", ".join(grocery))

