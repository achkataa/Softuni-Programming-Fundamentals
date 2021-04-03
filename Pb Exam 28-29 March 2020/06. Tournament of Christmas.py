days = int(input())
command = input()
win_or_lose = input()
money = 0
win_games = 0
lost_games = 0
games = 0
while command != "Finish":
    games += 1
    if win_or_lose == "win":
        money += 20
        win_games += 1
    else:
        money = 0
        lost_games += 1
    command = input()
    win_or_lose = input()
if win_games > lost_games:
    money += money * 0.1
else:
    money = money