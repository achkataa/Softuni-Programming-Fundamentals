input_operator = input()
input_first_number = int(input())
input_second_number = int(input())

def calculation(a, b, operator):
    if operator == "multiply":
        result = int(a * b)
        return result
    elif operator == "divide":
        result = int(a / b)
        return result
    elif operator == "add":
        result = int(a + b)
        return result
    elif operator == "subtract":
        result = int(a - b)
        return result

print(calculation(input_first_number, input_second_number, input_operator))