import re

line = input()


validation = r"(\+359\s2\s\d{3}\s\d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"


output = re.finditer(validation, line)

output = [p.group(0) for p in output]

print(", ".join(output))