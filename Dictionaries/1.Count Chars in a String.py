word = [w for w in input().split()]
result = {}

for char in word:
    for el in char:
        if not el in result:
            result[el] = 0
        result[el] += 1

for key, value in result.items():
    print(f"{key} -> {value}")
