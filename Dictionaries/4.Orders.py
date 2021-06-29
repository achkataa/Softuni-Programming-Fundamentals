command = input()
my_dict = {}

while command != "buy":
    data = command.split()
    name = data[0]
    price = float(data[1])
    quantity = int(data[2])

    if name not in my_dict:
        my_dict[name] = [price, quantity]

    else:
        my_dict[name] = [price, my_dict[name][1]]
        my_dict[name][1] += quantity


    command = input()

for key, value in my_dict.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
