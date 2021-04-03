text = input().split()
result = ""

for el in text:
    result += el * len(el)


print(result)
