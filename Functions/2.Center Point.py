x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def coordinate_system(a, b, c, d):
    first_sum = a + b
    second_sum = c + d
    if first_sum > second_sum:
        return f"{round(x2), round(y2)}"
    if second_sum > first_sum:
        return f"{round(x1), round(y1)}"
    else:
        return f"{round(x1), round(y1)}"

print(coordinate_system(x1, y1, x2, y2))