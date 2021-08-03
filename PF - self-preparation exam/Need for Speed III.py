n = int(input())

cars = {}

for i in range(n):
    car = input().split("|")
    car_name = car[0]
    mileage = int(car[1])
    fuel = int(car[2])
    cars[car_name] = [mileage, fuel]


command = input()

while command != "Stop":
    data = command.split(" : ")
    action = data[0]

    if action == "Drive":
        car = data[1]
        distance = int(data[2])
        fuel = int(data[3])

        if cars[car][1] >= fuel:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print(f"Not enough fuel to make that ride")

        if cars[car][0] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")


    elif action == "Refuel":
        car = data[1]
        fuel = int(data[2])

        if cars[car][1] + fuel > 75:
            print(f"{car} refueled with {75 - cars[car][1]} liters")
            cars[car][1] = 75
        else:
            cars[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")
    elif action == "Revert":
        car = data[1]
        kilometers = int(data[2])

        cars[car][0] -= kilometers

        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")




    command = input()

cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")