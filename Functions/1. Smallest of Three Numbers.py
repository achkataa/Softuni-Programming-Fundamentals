first_number = int(input())
second_number = int(input())
third_number = int(input())

def smallest_number(a, b, c):
    if a < b and a < c:
        result = a
    elif b < a and b < c:
        result = b
    elif c < a and c < b:
        result = c
    return result

print(smallest_number(first_number, second_number, third_number))
