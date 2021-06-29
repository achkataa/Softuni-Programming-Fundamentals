numbers = [int(num) for num in input().split()]

command = input()

while command != "End":
    index = int(command)

    if index < len(numbers):
        current_number = numbers[index]
        if numbers[index] != -1:
            numbers[index] = -1
        else:
            continue
        for i in range(len(numbers)):
            if numbers[i] == -1:
                continue
            elif numbers[i] > current_number:
                numbers[i] -= current_number
            else:
                numbers[i] += current_number
    command = input()


count = numbers.count(-1)

print(f"Shot targets: {count} -> {' '.join(str(num) for num in numbers) }")