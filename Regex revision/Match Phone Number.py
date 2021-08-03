import re

phone_numbers = input()

pattern = r"(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)"

result = re.finditer(pattern, phone_numbers)

print(', '.join([res.group(0) for res in result]))