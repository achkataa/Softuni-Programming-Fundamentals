import re
regex = re.compile('[@!#$%^&*()<>?/|{~: ]')
line = input().split(", ")
result = []

for el in line:
    if len(el) >= 3 and len(el) <= 16:
        if (regex.search(el) == None):
            result.append(el)
    else:
        continue

for char in result:
    print(char)
