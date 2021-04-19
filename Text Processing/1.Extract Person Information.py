n = int(input())

for number in range(n):
    line = input()
    name = line[line.index("@"):line.index("|")]
    age = line[line.index("#"):line.index("*")]
    result_name = name.split("@")
    result_age = age.split("#")
    print(f"{result_name[1]} is {result_age[1]} years old.")



