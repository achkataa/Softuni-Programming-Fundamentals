import sys
breads = int(input())
max = - sys.maxsize
max_name = ""
current_marks = 0
total_marks = 0
for bread in range(1, breads + 1):
    name = input()
    command = input()
    current_marks = 0
    while command != "Stop":
        marks = int(command)
        current_marks += marks
        total_marks = current_marks
        command = input()
    print(f"{name} has {current_marks} points.")

    if current_marks > max:
        max_name = name
        max = current_marks
        print(f"{name} is the new number 1!")

print(f"{max_name} won competition with {max} points!")



