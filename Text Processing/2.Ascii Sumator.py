first_char = ord(input())
second_char = ord(input())

line = input()
sum = 0
for char in line:
    if second_char > ord(char) > first_char:
        sum += ord(char)

print(sum)