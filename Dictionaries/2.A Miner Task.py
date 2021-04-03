command = input()

result = {}

while command != "stop":
    quantity = int(input())
    if command in result:
        result[command] += quantity
    else:
        result[command] = quantity


    command = input()

for key, value in result.items():
    print(f"{key} -> {value}")