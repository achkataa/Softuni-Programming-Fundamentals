days_of_the_plunder = int(input())
daily_plunder = int(input())
expected_plunder = float(input())


gathered_plunder = 0

for day in range(1, days_of_the_plunder + 1):
    gathered_plunder += daily_plunder

    if day % 3 == 0:
        gathered_plunder += daily_plunder * 0.5

    if day % 5 == 0:
        gathered_plunder = gathered_plunder - (gathered_plunder * 0.3)

if gathered_plunder >= expected_plunder:
    print(f"Ahoy! {gathered_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {(gathered_plunder * 100) / expected_plunder:.2f}% of the plunder.")
