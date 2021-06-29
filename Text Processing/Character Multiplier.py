line = input().split()

first_string = line[0]
second_string = line[1]
result = 0
counter = 0

if len(first_string) >= len(second_string):
    for el in range(len(first_string)):
        if counter < len(second_string):
            result += ord(first_string[el]) * ord(second_string[counter])
            counter += 1
        else:
            result += ord(first_string[el])
else:
    for el in range(len(second_string)):
        if counter < len(first_string):
            result += ord(first_string[el]) * ord(second_string[counter])
            counter += 1
        else:
            result += ord(second_string[el])


print(result)
