elements = [el.lower() for el in input().split()]

result = {}

for el in elements:
    result[el] = elements.count(el)

result = [el for el in result if result[el] % 2 != 0]
print(" ".join(result))



