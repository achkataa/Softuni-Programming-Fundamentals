import re

line = input()
result = []
price = 0

furniture = r"(^|(?<=\s))>>(?P<Name>[A-Za-z]+)<<(?P<Price>\d+(\.\d+)?)!(?P<Quantity>\d+)($|(?=\s))"

while line != "Purchase":
    match = re.finditer(furniture, line)
    if match:
        for m in match:
            d = m.groupdict()
            result.append(d["Name"])
            price += float(d["Price"]) * int(d["Quantity"])

    line = input()

print("Bought furniture:")
for i in result:
    print(i)

print(f"Total money spend: {price:.2f}")




