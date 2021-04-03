first_player_eggs = int(input())
second_player_eggs = int(input())
command = input()

while command != "End of battle":
    if command == "one":
        second_player_eggs = second_player_eggs - 1
    else:
        first_player_eggs = first_player_eggs - 1
    if first_player_eggs == 0:
        print(f"Player one is out of eggs. Player two has {second_player_eggs} eggs left.")
        break
    if second_player_eggs == 0:
        print(f"Player two is out of eggs. Player one has {first_player_eggs} eggs left.")
        break
    command = input()
else:
    print(f"Player one has {first_player_eggs} eggs left.")
    print(f"Player two has {second_player_eggs} eggs left.")



