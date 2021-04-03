string_of_nums = input()
formatted = string_of_nums.split(" ")
int_nums = []
result = []

for char in formatted:
    int_nums.append(int(char))

for char in int_nums:
    if char <= 0:
        result.append(abs(char))
    else:
        result.append(-char)

print(result)













