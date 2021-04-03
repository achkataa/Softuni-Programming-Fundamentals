import re
line = input()

pattern = r"(^|(?<=\s))[A-Za-z0-9]+[.\_-]?[A-Za-z0-9]+@[A-Za-z0-9]+\-?[A-Za-z]+(\.[a-zA-Z]+\-?[a-zA-Z]+)+"

result = re.finditer(pattern, line)

for res in result:
    print(res.group())