towns_command = input()

towns = {}

while towns_command != "Sail":
    data = towns_command.split("||")
    town_name = data[0]
    population = int(data[1])
    gold = int(data[2])

    if town_name in towns:
        towns[town_name][0] += population
        towns[town_name][1] += gold

    else:
        towns[town_name] = [population, gold]

    towns_command = input()

action_command = input()

while action_command != "End":
    splitted_data = action_command.split("=>")
    action = splitted_data[0]

    if action == "Plunder":
        name = splitted_data[1]
        town_gold = int(splitted_data[3])
        town_population = int(splitted_data[2])
        towns[name][0] -= town_population
        towns[name][1] -= town_gold

        print(f"{name} plundered! {town_gold} gold stolen, {town_population} citizens killed.")

        if towns[name][0] == 0 or towns[name][1] == 0:
            del towns[name]
            print(f"{name} has been wiped off the map!")

    elif action == "Prosper":
        town_name = splitted_data[1]
        gold_in_town = int(splitted_data[2])

        if gold_in_town > 0:
            towns[town_name][1] += gold_in_town
            print(f"{gold_in_town} gold added to the city treasury. {town_name} now has {towns[town_name][1]} gold.")

        else:
            print(f"Gold added cannot be a negative number!" )

    action_command = input()

if len(towns) == 0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    towns = dict(sorted(towns.items(), key=lambda x: (-x[1][1], x[0])))

    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for key, value in towns.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
