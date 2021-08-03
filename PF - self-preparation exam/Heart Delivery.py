neighborhood = [int(house) for house in input().split("@")]

command = input()

current_index = 0

while command != "Love!":
    data = command.split()
    length = int(data[1])

    current_index += length

    if current_index >= len(neighborhood):
        current_index = 0

    if neighborhood[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        neighborhood[current_index] -= 2
        if neighborhood[current_index] == 0:
            print(f"Place {current_index} has Valentine's day.")

    command = input()


print(f"Cupid's last position was {current_index}.")
if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len([house for house in neighborhood if house > 0])} places.")






