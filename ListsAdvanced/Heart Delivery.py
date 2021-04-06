neighborhood = [int(house) for house in input().split("@")]

command = input()
current_index = 0
while command != "Love!":
    data = command.split()
    length = int(data[1])

    end = neighborhood.index(neighborhood[current_index]) + length


    if end < len(neighborhood):
        if neighborhood[end] == 0:
            print(f"Place {end} already had Valentine's day.")
        neighborhood[end] -= 2
        if neighborhood[end] <= 0:
            print(f"Place {end} has Valentine's day.")
    else:
        current_index = 0
        if neighborhood[0] == 0:
            print(f"Place {0} already had Valentine's day.")
        else:
            neighborhood[0] -= 2
            if neighborhood[0] <= 0:
                print(f"Place {0} has Valentine's day.")




        command = input()
        continue
    current_index += length
    command = input()

failed = 0
print(f"Cupid's last position was {current_index}.")

for house in neighborhood:
    if house != 0:
        failed += 1

if failed > 0:
    print(f"Cupid has failed {failed} places.")
else:
    print("Mission was successful.")







