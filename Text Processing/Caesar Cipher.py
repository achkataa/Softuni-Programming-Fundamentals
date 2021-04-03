line = input()
result = ""
for el in range(len(line)):
    encrypt = ord(line[el])
    result += chr(encrypt + 3)

print(result)