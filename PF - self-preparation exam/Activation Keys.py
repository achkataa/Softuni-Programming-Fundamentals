raw_key = input()

command = input()

while command != "Generate":
    data = command.split(">>>")
    operation = data[0]

    if operation == "Contains":
        substring = data[1]
        if substring in raw_key:
            print(f"{raw_key} contains {substring}")
        else:
            print("Substring not found!")


    elif operation == "Flip":
        upper_or_lower = data[1]
        start = int(data[2])
        stop = int(data[3])
        raw_keyy = list(raw_key)
        if upper_or_lower == "Upper":
            for index in range(len(raw_key)):
                if start <= index < stop:
                    raw_keyy[index] = raw_key[index].upper()
        else:
            for index in range(len(raw_key)):
                if start <= index < stop:
                    raw_keyy[index] = raw_key[index].lower()

        raw_keyy = "".join(raw_keyy)
        raw_key = raw_keyy
        print(raw_key)


    elif operation == "Slice":
        start = int(data[1])
        stop = int(data[2])
        raw_key = list(raw_key)
        del raw_key[start:stop]
        raw_key = "".join(raw_key)
        print(raw_key)


    command = input()

print(f"Your activation key is: {raw_key}")