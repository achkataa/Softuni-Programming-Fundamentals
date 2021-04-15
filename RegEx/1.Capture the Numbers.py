import re

line = input()
total_result = []
validation = r"\d+"
while line:
    match = re.findall(validation, line)
    if match:
        total_result.extend(match)
    line = input()

print(*total_result)