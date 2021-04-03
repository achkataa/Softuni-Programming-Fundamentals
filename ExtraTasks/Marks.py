students = int(input())
excellent = 0
verygood = 0
good = 0
average = 0
all_marks = 0
for student in range(1, students + 1):
    mark = float(input())
    if mark >= 5:
        excellent = excellent + 1
    elif mark >= 4 and mark <= 4.99:
        verygood = verygood + 1
    elif mark >= 3 and mark <= 3.99:
        good = good + 1
    elif mark >= 2 and mark <= 2.99:
        average = average + 1
    all_marks += mark
print(f"Top students: {excellent * 100 / students:.2f}%")
print(f"Between 4.00 and 4.99: {verygood * 100 / students:.2f}%")
print(f"Between 3.00 and 3.99: {good * 100 / students:.2f}%")
print(f"Fail: {average * 100 / students:.2f}%")
print(f"Average: {all_marks / students:.2f}")
