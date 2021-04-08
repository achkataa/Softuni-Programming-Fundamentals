data_type = input()
data = input()

def calculate_data(a, b):
    if a == "int":
        b = int(b)
        result = b * 2
        return result
    elif a == "real":
        b = float(b)
        result = f"{b * 1.5:.2f}"
        return result
    else:
        result = f"${b}$"
        return result

print(calculate_data(data_type, data))
