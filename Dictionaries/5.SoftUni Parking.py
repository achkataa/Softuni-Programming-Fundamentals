n = int(input())
result = {}

for num in range(n):
    command = input().split()

    if command[0] == "unregister":
        username = command[1]
        if username not in result:
            print(f"ERROR: user {username} not found")
        else:
            del result[username]
            print(f"{username} unregistered successfully")
    else:
        username = command[1]
        licence_plate = command[2]
        if username in result:
            print(f"ERROR: already registered with plate number {result[username]}")
        else:
            result[username] = licence_plate
            print(f"{username} registered {licence_plate} successfully")

for key, value in result.items():
    print(f"{key} => {value}")