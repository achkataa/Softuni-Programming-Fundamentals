import re
line = input()

date = r"(?P<Day>\d{2})(?P<Separator>[\./-])(?P<Month>[A-Z][a-z]{2})(?P=Separator)(?P<Year>\d{4})"

result = re.finditer(date, line)

for res in result:
   d = res.groupdict()
   print(f"Day: {d['Day']}, Month: {d['Month']}, Year: {d['Year']}")




