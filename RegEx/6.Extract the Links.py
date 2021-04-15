import re
line = input()

valid_mail = r"(^|(?<=\s))\bw{3}.[A-Za-z0-9\-]+(\.[a-z]+)+"

while line:
    result = re.finditer(valid_mail, line)

    for res in result:
        print(res.group())

    line = input()
