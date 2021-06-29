import re
text = input()

validation = r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b"

names = re.findall(validation, text)

print(" ".join(names))
