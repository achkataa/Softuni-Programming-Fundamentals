detergent_bottles = int(input())
detergent_amount = detergent_bottles * 750
clean_plates_counter = 0
clean_pots_counter = 0
detergent_needed = 0
load = 1

command = input()
while command != "End":
    dishes = int(command)
    if load % 3 == 0:
        detergent_needed = dishes * 15
        detergent_amount -= detergent_needed
        clean_pots_counter += dishes
    else:
        detergent_needed = dishes * 5
        detergent_amount -= detergent_needed
        clean_plates_counter += dishes

    if detergent_amount < 0:
        print(f"Not enough detergent, {abs(detergent_amount)} ml. more necessary!")
        break
    load += 1
    command = input()
else:
    print("Detergent was enough!")
    print(f"{clean_plates_counter} dishes and {clean_pots_counter} pots were washed.")
    print(f"Leftover detergent {detergent_amount} ml.")



