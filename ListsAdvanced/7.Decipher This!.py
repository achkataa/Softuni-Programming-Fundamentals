secret_message = [word for word in input().split()]
digits = []
for word in secret_message:
    for char in word:
        if char.isdigit():
            digits.append(char)
            number = "".join(digits)
            letter = chr(int(number))
            