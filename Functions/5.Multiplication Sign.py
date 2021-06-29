from operator import mul

num1 = int(input())
num2 = int(input())
num3 = int(input())

def multiplication_sign(a, b, c):
    result = mul(a, b) * c

    if result < 0:
        return "negative"
    elif result > 0:
        return "positive"
    else:
        return "zero"

print(multiplication_sign(num1, num2, num3))