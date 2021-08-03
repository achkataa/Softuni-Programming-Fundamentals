secret_message = input()

command = input()

while command != "Reveal":
    data = command.split(":|:")
    action = data[0]

    if action == "InsertSpace":
        index = int(data[1])
        part = secret_message[:index]
        secret_message = part + " " + secret_message[index:]
        print(secret_message)
    elif action == "Reverse":
        substring = data[1]
        if substring in secret_message:
            secret_message = secret_message.replace(substring, "", 1)
            secret_message += substring[::-1]
            print(secret_message)
        else:
            print("error")
    elif action == "ChangeAll":
        substring = data[1]
        replacement = data[2]

        secret_message = secret_message.replace(substring, replacement)
        print(secret_message)

    command = input()


print(f"You have a new text message: {secret_message}")