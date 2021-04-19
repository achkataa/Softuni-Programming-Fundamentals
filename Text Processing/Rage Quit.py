line = input()
result = ""
current = ""
digit = ""
index = 0
while index < len(line):
    if not line[index].isdigit():
        current += line[index]
        index += 1

    else:
        while line[index].isdigit():
            digit += line[index]
            index += 1
            if index >= len(line):
                break

        current = current.upper() * int(digit)
        result += current
        current = ""
        digit = ""


print(f"Unique symbols used: {len(set(result))}")
print(result)
