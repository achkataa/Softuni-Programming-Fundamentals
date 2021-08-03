import re

pattern = r"(?P<Day>\d{2})(?P<Separator>[\./-])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})"

dates = input()

result = re.finditer(pattern, dates)

for res in result:
    dict_result = res.groupdict()
    print(f"Day: {dict_result['Day']}, Month: {dict_result['Month']}, Year: {dict_result['Year']}")