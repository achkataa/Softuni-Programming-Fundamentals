import math
students = int(input())
lectures = int(input())
bonus = int(input())
attendances_lst = []
max_bonus = 0


if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')

else:
    for student in range(students):
        attendances = int(input())
        attendances_lst.append(attendances)

    max_bonus = math.ceil((max(attendances_lst) / lectures) * (5 + bonus))

    print(f'Max Bonus: {max_bonus}.')
    print(f'The student has attended {max(attendances_lst)} lectures.')

