stadium_capacity = int(input())
fans_number = int(input())
fans_a = 0
fans_b = 0
fans_c = 0
fans_d = 0
percent_stadium = 0
for fan in range(1, fans_number + 1):
    sector = input()
    if sector == "A":
        fans_a += 1
    elif sector == "B":
        fans_b += 1
    elif sector == "V":
        fans_c += 1
    elif sector == "G":
        fans_d += 1

print(f"{fans_a / fans_number * 100:.2f}%")
print(f"{fans_b / fans_number * 100:.2f}%")
print(f"{fans_c / fans_number * 100:.2f}%")
print(f"{fans_d / fans_number * 100:.2f}%")
print(f"{fans_number / stadium_capacity * 100:.2f}%")


