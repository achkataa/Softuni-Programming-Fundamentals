happiness = [int(happy_person) for happy_person in input().split()]
factor = int(input())

happiness_by_factor = [number * factor for number in happiness]


people = [person for person in happiness_by_factor if person >= sum(happiness_by_factor) / len(happiness_by_factor) ]

if len(people) >= len(happiness) / 2:
    print(f"Score: {len(people)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(people)}/{len(happiness)}. Employees are not happy!")