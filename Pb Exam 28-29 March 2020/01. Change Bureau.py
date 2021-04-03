bitcoin = int(input())
iuna = float(input())
commission = float(input())

bitcoin_counter = 1168 * bitcoin


iuna_counter = (0.15 * iuna) * 1.76





total = (bitcoin_counter + iuna_counter) / 1.95




commission_counter = total / 100 * commission




result = total - commission_counter
print(f"{result:.2f}")

