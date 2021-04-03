zeros = [0 for num in range(1, 11)]
command = input()

while command != "End":
    data = command.split("-")

    for el in data[0]:
        zeros.insert(int(data[0]), data[1])

    command = input()

result = [index for index in zeros if index != 0]

print(result)


