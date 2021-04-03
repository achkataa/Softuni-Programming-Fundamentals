input_password = input()

def validator(password):
    is_valid = True
    if len(password) < 6 or len(password) > 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    for el in password:
        if el.isdigit() == False:
            if el.isalpha() == False:
                is_valid = False
                print("Password must consist only of letters and digits")
                break
    digits = 0
    for el in password:
        if el.isdigit():
            digits += 1
    if digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    return is_valid


is_valid = validator(input_password)

if is_valid:
    print("Password is valid")