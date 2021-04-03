employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
people = int(input())
hours = 0

all_employees_work_per_hour = employee1 + employee2 + employee3

while people > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    people -= all_employees_work_per_hour

print(f"Time needed: {hours}h.")


