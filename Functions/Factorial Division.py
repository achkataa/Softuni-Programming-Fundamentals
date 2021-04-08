factorial = int(input())
second_number = int(input())

def division(a, b,):
    result = 1
    second_result = 1
    for number in range(factorial, 1 - 1, -1):
        result *= number
    for number_2 in range(second_number, 1 - 1, -1):
        second_result *= number_2

    print(f"{result / second_result:.2f}")


division(factorial, second_number)