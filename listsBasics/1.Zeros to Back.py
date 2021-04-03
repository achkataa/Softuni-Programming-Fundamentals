numbers = input().split(", ")
result = []

for number in numbers:
    number = int(number)
    result.append(number)

for number in result:
    if number == 0:
        result.append(result.pop(result.index(number)))

print(result)