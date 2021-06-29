line = input().split()
my_dict = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8',
           'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17',
           'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'
           }
sum = 0
for el in line:
    digit = int(el[1:-1])

    if el[0].islower():
        digit *= int(my_dict[el[0].lower()])
    else:
        digit /= int(my_dict[el[0].lower()])

    if el[-1].islower():
        digit += int(my_dict[el[-1].lower()])
    else:
        digit -= int(my_dict[el[-1].lower()])

    sum += digit

print(f"{sum:.2f}")