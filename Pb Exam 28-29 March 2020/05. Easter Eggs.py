eggs = int(input())
max_eggs_color = ""
max_eggs_number = 0
red_eggs_counter = 0
orange_eggs_counter = 0
blue_eggs_counter = 0
green_eggs_counter = 0

for egg in range(1, eggs + 1):
    color = input()
    if color == "red":
        red_eggs_counter += 1
    elif color == "orange":
        orange_eggs_counter += 1
    elif color == "blue":
        blue_eggs_counter += 1
    elif color == "green":
        green_eggs_counter += 1

if red_eggs_counter > orange_eggs_counter and red_eggs_counter > blue_eggs_counter and red_eggs_counter > green_eggs_counter:
    max_eggs_color = "red"
    max_eggs_number = red_eggs_counter
elif orange_eggs_counter > red_eggs_counter and orange_eggs_counter > blue_eggs_counter and orange_eggs_counter > green_eggs_counter:
    max_eggs_color = "orange"
    max_eggs_number = orange_eggs_counter
elif blue_eggs_counter > red_eggs_counter and blue_eggs_counter > orange_eggs_counter and blue_eggs_counter > green_eggs_counter:
    max_eggs_color = "blue"
    max_eggs_number = blue_eggs_counter
elif green_eggs_counter > red_eggs_counter and green_eggs_counter > orange_eggs_counter and green_eggs_counter > blue_eggs_counter:
    max_eggs_color = "green"
    max_eggs_number = green_eggs_counter



print(f"Red eggs: {red_eggs_counter}")
print(f"Orange eggs: {orange_eggs_counter}")
print(f"Blue eggs: {blue_eggs_counter}")
print(f"Green eggs: {green_eggs_counter}")
print(f"Max eggs: {max_eggs_number} -> {max_eggs_color}")


