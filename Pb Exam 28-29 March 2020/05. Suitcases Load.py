trunk_capacity = float(input())
command = input()
suitcases_counter = 0
trunk_busy_capacity = 0

while command != "End":
    command = float(command)

    trunk_busy_capacity += command
    if trunk_busy_capacity > trunk_capacity:
        print("No more space!")
        print(f"Statistic: {suitcases_counter} suitcases loaded.")
        break
    suitcases_counter += 1
    command = input()
else:
    print("Congratulations! All suitcases are loaded!")
    print(f"Statistic: {suitcases_counter} suitcases loaded.")
