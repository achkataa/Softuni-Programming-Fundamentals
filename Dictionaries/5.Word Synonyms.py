n = int(input())

result = {}

for w in range(n):
    word = input()
    synonym = input()
    if word not in result:
        result[word] = synonym
    else:
        result[word] += f", {synonym}"

for key, value in result.items():
    print(f"{key} - {value}")