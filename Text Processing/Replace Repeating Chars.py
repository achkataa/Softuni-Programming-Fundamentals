line = input()
result = []

for i in range(len(line)):
    if i == 0:
        result.append(line[i])
        continue

    if line[i] != line[i - 1]:
        result.append(line[i])
    else:
        continue

print("".join(result))

