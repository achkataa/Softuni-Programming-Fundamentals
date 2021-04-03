command = input()
result = {}

while command != "end":
    data = command.split(" : ")
    course = data[0]
    student = data[1]

    if course not in result:
        result[course] = [student]
    else:
        result[course].append(student)

    command = input()


for k in sorted(result, key=lambda k: len(result[k]), reverse=True):
    print(f"{k}: {len(result[k])}")
    for val in sorted(result[k]):
        print(f"-- {val}")


