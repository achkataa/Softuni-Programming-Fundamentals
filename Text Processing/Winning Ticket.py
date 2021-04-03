tickets = input().split(", ")
winning_symbols = ["@", "#", "$", "^"]

def is_jackpot(ls, rs):
    if ls == rs:
        for symbol in winning_symbols:
            if symbol * 10 == rs:
                print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
                return True
    return False

def is_no_match(ls, rs):
    is_true_l = False
    is_true_r = False
    for symbol in winning_symbols:
        if symbol * 6 in ls:
            is_true_l = True
        if symbol * 6 in rs:
            is_true_r = True
    if is_true_r and is_true_l == True:
        return False
    else:
        print(f'ticket "{ticket}" - no match')
        return True



def is_winning(ls, rs):
    for symbol in winning_symbols:
        if symbol * 6 in ls and symbol * 6 in rs:
            count_l = ls.count(symbol)
            count_r = rs.count(symbol)
            count = min(count_l, count_r)
            print(f'ticket "{ticket}" - {count}{symbol}')
            return True



for t in tickets:
    ticket = t.strip()
    if len(ticket) != 20:
        print("invalid ticket")
        continue
    left_side = ticket[0:10]
    right_side = ticket[10:20]

    if is_jackpot(left_side, right_side):
        continue

    if is_no_match(left_side, right_side):
        continue

    if is_winning(left_side, right_side):
        continue
