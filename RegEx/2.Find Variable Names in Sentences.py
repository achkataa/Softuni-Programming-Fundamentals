import re

line = input()

string = r"(?<=\b_)[A-Za-z0-9]+\b"

validation = re.findall(string, line)

print(",".join(validation))