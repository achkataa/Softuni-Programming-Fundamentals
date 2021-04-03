factor = int(input())
count = int(input())
multiply = factor * count

result = []

for number in range(1, multiply + 1):
    if number % factor == 0:
        result.append(number)
print(result)