people = int(input())
lift = [int(x) for x in input().split()]
full = [4 for num in lift]

index = 0
while people > 0 and lift != full:
    while lift[index] < 4:
        if people > 0:
            lift[index] += 1
            people -= 1
    index += 1


def print_lift(list):
    print(' '.join(str(wagon) for wagon in list))


if people < 1 and lift != full:
    print("The lift has empty spots!")
    print_lift(lift)
elif people > 0 and lift == full:
    print(f"There isn't enough space! {people} people in a queue!")
    print_lift(lift)
else:
    print_lift(lift)