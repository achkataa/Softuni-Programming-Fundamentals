elements = input().split()

command = input()

counter = 0

def check_if_indexes_are_valid(elements, index1, index2):
    if len(elements) > index1 > -1 and len(elements) > index2 > -1:
        return True
    return False



while command != "end":
    counter += 1
    data = command.split()
    index1 = int(data[0])
    index2 = int(data[1])

    if check_if_indexes_are_valid(elements, index1, index2):
        if elements[index1] == elements[index2]:
            print(f"Congrats! You have found matching elements - {elements[index1]}!")
            first_element = elements[index1]
            second_element = elements[index2]
            elements.remove(first_element)
            elements.remove(second_element)
        else:
            print("Try again!")

    else:
        print("Invalid input! Adding additional elements to the board")
        middle_index = len(elements) // 2
        element = f"-{counter}a"
        elements.insert(middle_index, element)
        elements.insert(middle_index + 1, element)

    if not elements:
        print(f"You have won in {counter} turns!")
        exit(0)

    command = input()

print("Sorry you lose :(")
print(' '.join(str(el) for el in elements))

