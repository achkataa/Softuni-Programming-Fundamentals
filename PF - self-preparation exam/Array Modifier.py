array = [int(el) for el in input().split()]

command = input()

def swap(list, index1, index2):
    list[index1], list[index2] = list[index2], list[index1]
    return list

def multiply(list, index1, index2):
    product = list[index1] * list[index2]
    list[index1] = product
    return list

def decrease(list):
    for i in range(len(list)):
        list[i] = list[i] - 1
    return list

while command != "end":
    data = command.split()
    action = data[0]

    if action == "swap":
        first_index = int(data[1])
        second_index = int(data[2])
        swap(array, first_index, second_index)
    elif action == "multiply":
        first_index = int(data[1])
        second_index = int(data[2])
        multiply(array, first_index, second_index)
    elif action == "decrease":
        decrease(array)

    command = input()

print(', '.join(str(el) for el in array))