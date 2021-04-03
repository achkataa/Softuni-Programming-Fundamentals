people = int(input())
wagons = [int(wagon) for wagon in input().split()]
full = [4 for num in wagons]
index = 0


for wagon in wagons:
    if people <= 0:
        break
    if wagons == full:
        break
    while wagons[index] < 4:
        wagons[index] += 1
        people -= 1
    index += 1


# if people <= 0:
#     break
# if wagons == full:
#     break
#     else:
#         break
# index += 1





if people <= 0 and wagons != full:
    print("The lift has empty spots!")
    wagons = [str(wagon) for wagon in wagons]
    print(" ".join(wagons))
elif people > 0 and wagons == full:
    print(f"There isn't enough space! {people} people in a queue!")
    wagons = [str(wagon) for wagon in wagons]
    print(" ".join(wagons))
else:
    wagons = [str(wagon) for wagon in wagons]
    print(" ".join(wagons))


