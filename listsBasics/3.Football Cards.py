cards = input().split(" ")
team_a_players = 11
team_b_players = 11
set_1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
set_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}


for card in cards:
    team, numbers = card.split("-")
    number = int(numbers)
    if team == "A":
        if number in set_1:
            set_1.remove(number)
        team_a_players -= 1
    elif team == "B":
        if number in set_2:
            set_2.remove(number)
        team_b_players -= 1

print(f"Team A - {team_a_players}; Team B - {team_b_players}")
if team_b_players < 7 or team_b_players < 7:
    print(f"Game was terminated")


