import re

line = input()

numbers = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"

result = re.finditer(numbers, line)

result = [res.group() for res in result]

print(*result)