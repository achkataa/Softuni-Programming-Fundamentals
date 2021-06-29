first_number = int(input())
second_number = int(input())
third_number = int(input())

def sum_numbers(a, b, c):
    sum_result = a + b
    total_result = sum_result - c
    return total_result

print(sum_numbers(first_number, second_number, third_number))
