foo = '\\'

line = input().split(foo)

result = line[-1].split(".")

print(f"File name: {result[0]}")
print(f"File extension: {result[1]}")