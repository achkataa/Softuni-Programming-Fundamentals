import sys
import math
max = -sys.maxsize
bigger_attendance = 0
students = int(input())
lectures = int(input())
bonus = int(input())

for student in range(1, students + 1):
    attendance = int(input())

    total_bonus = (attendance / lectures) * (5 + bonus)

    if total_bonus > max:
        max = total_bonus
        bigger_attendance = attendance

print(f"Max Bonus: {math.ceil(max)}.")
print(f"The student has attended {bigger_attendance} lectures.")



