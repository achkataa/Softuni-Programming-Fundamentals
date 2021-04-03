needed_sum = int(input())
raised_sum = 0
sum_paid_in_cash = 0
sum_paid_with_card = 0
successful_card_paid = 0
successful_cash_paid = 0

pay = 1

command = input()

while command != "End":
    price = int(command)
    if pay % 2 == 0:
        if price < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            raised_sum += price
            sum_paid_with_card += price
            successful_card_paid += 1
    else:
        if price > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            raised_sum += price
            sum_paid_in_cash += price
            successful_cash_paid += 1
    if raised_sum >= needed_sum:
        print(f"Average CS: {sum_paid_in_cash / successful_cash_paid:.2f}")
        print(f"Average CC: {sum_paid_with_card / successful_card_paid:.2f}")
        break
    pay += 1
    command = input()
else:
    print(f"Failed to collect required money for charity.")



