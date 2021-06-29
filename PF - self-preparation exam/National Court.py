first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

people = int(input())
hours = 0
total_efficiency = first_employee + second_employee + third_employee
while people > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1
    people -= total_efficiency

print(f"Time needed: {hours}h.")


