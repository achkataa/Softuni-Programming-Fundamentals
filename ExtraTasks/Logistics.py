load_count = int(input())
all_loads = 0
one_ton_price = 0
total_price = 0
bus = 0
truck = 0
train = 0
for load in range(1 , load_count + 1):
    ton = int(input())
    all_loads += ton
    if ton <= 3:
        bus += ton
        one_ton_price = 200
        total_price = total_price + (one_ton_price * ton)
    elif ton >= 4 and ton <= 11:
        truck += ton
        one_ton_price = 175
        total_price = total_price + (one_ton_price * ton)
    elif ton >= 12:
        train += ton
        one_ton_price = 120
        total_price = total_price + (one_ton_price * ton)

total_loads = total_price / all_loads
print(f"{total_loads:.2f}")
print(f"{bus / all_loads * 100:.2f}%")
print(f"{truck / all_loads * 100:.2f}%")
print(f"{train / all_loads * 100:.2f}%")




