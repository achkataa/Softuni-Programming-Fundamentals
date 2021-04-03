guests = int(input())
kuvert_price_for_one_person = float(input())
budget = float(input())

if guests >= 10 and guests <= 15:
    kuvert_price_for_one_person = kuvert_price_for_one_person - (kuvert_price_for_one_person * 0.15)
elif guests > 15 and guests <= 20:
    kuvert_price_for_one_person = kuvert_price_for_one_person - (kuvert_price_for_one_person * 0.2)
elif guests > 20:
    kuvert_price_for_one_person = kuvert_price_for_one_person - (kuvert_price_for_one_person * 0.25)

cake = budget * 0.1

total_sum = (guests * kuvert_price_for_one_person) + cake

if total_sum > budget:
    print(f"No party! {total_sum - budget:.2f} leva needed.")
else:
    print(f"It is party time! {budget - total_sum:.2f} leva left.")

