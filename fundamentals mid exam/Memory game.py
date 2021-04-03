import math
elements = [el for el in input().split()]


moves = 0
command = input()

while command != "end":
    moves += 1
    data = command.split()
    index1 = int(data[0])
    index2 = int(data[1])

    if index1 < 0 or index1 > len(elements) or index2 < 0 or index2 > len(elements):
        midpoint = math.floor(len(elements) / 2)
        elements.insert(midpoint, f"-{moves}a")
        elements.insert(midpoint, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")


    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        unwanted = {elements[index1], elements[index2]}
        elements = [ele for ele in elements if ele not in unwanted]
    elif elements[index1] != elements[index2]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        exit(0)
    command = input()


print("Sorry you lose :(")
print(" ".join(elements))



