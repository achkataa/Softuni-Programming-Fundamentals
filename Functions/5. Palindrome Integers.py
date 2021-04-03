input_numbers = input().split(", ")

def palindrome_or_not(numbers):
    for num in input_numbers:
        if num == num[::-1]:
            print("True")
        else:
            print("False")

palindrome_or_not(input_numbers)