number = int(input())
odd_sum = 0
even_sum = 0

def sum_digits(n, input_even_sum, input_odd_sum):
    result = [int(d) for d in str(n)]
    for number in result:
        if number % 2 == 0:
            input_even_sum += number
        else:
            input_odd_sum += number
    result_number = f"Odd sum = {input_odd_sum}, Even sum = {input_even_sum}"
    return result_number


print(sum_digits(number, odd_sum, even_sum))



