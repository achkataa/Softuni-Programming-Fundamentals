input_text = input()
repetitions = int(input())

def repeat(text, number):
    result = f"{text * number}"
    return result

print(repeat(input_text, repetitions))

