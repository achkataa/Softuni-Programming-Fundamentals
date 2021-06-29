import math
students = int(input())
lectures = int(input())
initial_bonus = int(input())

students_bonuses = {}

if lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')

else:
    for i in range(students):
        attendance = int(input())

        total_bonus = attendance / lectures * (5 + initial_bonus)
        students_bonuses[math.ceil(total_bonus)] = attendance
    print(f"Max Bonus: {max(students_bonuses)}.")
    print(f"The student has attended {students_bonuses[max(students_bonuses)]} lectures.")

