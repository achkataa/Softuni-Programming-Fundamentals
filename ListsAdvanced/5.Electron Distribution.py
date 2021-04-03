electrons = int(input())
result = []
counter = 0

while electrons > 0:
    counter += 1
    command = ((2 * counter) ** 2) / 2
    if electrons < command:
        result.append(int(electrons))
        break
    result.append(int(command))
    electrons -= command

print(result)





