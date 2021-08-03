initial_string = input()

command = input()

while command != "Done":
    data = command.split()
    action = data[0]

    if action == "TakeOdd":
        initial_string = ''.join([initial_string[index] for index in range(len(initial_string)) if index % 2 != 0])
        print(initial_string)
    elif action == "Cut":
        index = int(data[1])
        length = int(data[2])
        part = initial_string[index:index+length]
        initial_string = initial_string.replace(part, "", 1)
        print(initial_string)
    elif action == "Substitute":
        substring = data[1]
        substitute = data[2]
        if substring in initial_string:
            initial_string = initial_string.replace(substring, substitute)
            print(initial_string)
        else:
            print("Nothing to replace!")



    command = input()


print(f"Your password is: {initial_string}")