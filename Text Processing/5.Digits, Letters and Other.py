line = input()

result = {"digits": "", "letters": "", "elements": ""}


for chr in line:
    if chr.isdigit():
        result["digits"] += chr
    elif chr.isalpha():
        result["letters"] += chr
    else:
        result["elements"] += chr

for key, value in result.items():
    print(value)

