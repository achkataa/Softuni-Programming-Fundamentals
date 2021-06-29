n = int(input())
average_grade = 0

my_dict = {}

for num in range(n):
    student = input()
    grade = float(input())

    if student not in my_dict:
        my_dict[student] = [grade]
    else:
        my_dict[student].append(grade)


final_dict = {key: my_dict[key] for key in my_dict if sum(my_dict[key]) / len(my_dict[key]) >= 4.50}

for key, value in final_dict.items():
    average_grade = sum(value) / len(value)
    final_dict[key] = average_grade


for key, value in sorted(final_dict.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} -> {value:.2f}")


