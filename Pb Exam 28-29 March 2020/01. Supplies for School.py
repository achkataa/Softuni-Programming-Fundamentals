pens = int(input())
markers = int(input())
washing_powder = float(input())
discount = int(input())

all_pans = pens * 5.80
all_markers = markers * 7.20
all_mashing_powder = washing_powder * 1.20

all_price = all_pans + all_markers + all_mashing_powder

total_price = all_price - ((all_price * discount) / 100)

print(f"{total_price:.3f}")