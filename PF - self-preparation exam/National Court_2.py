employee1 = int(input())
employee2 = int(input())
employee3 = int(input())


people = int(input())
hours = 0

total_efficiency = employee1 + employee2 + employee3

while people > 0:
    hours += 1
    people -= total_efficiency
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")

