command = input()
my_dict = {}

while command != "statistics":
    data = command.split(": ")
    key = data[0]
    value = int(data[1])
    if key in my_dict:
        my_dict[key] += value
    else:
        my_dict[key] = value

    command = input()

print("Products in stock:")

for key, value in my_dict.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(my_dict.keys())}")
print(f"Total Quantity: {sum(my_dict.values())}")
