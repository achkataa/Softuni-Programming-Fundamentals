n = int(input())

heroes = {}

for i in range(n):
    hero = input().split()
    name = hero[0]
    hp = int(hero[1])
    mp = int(hero[2])

    heroes[name] = [hp, mp]


command = input()

while command != "End":
    data = command.split(" - ")
    action = data[0]

    if action == "CastSpell":
        hero_name = data[1]
        mp_needed = int(data[2])
        spell_name = data[3]

        if heroes[hero_name][1] >= mp_needed:
            heroes[hero_name][1] -= mp_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        hero_name = data[1]
        damage = int(data[2])
        attacker = data[3]

        heroes[hero_name][0] -= damage

        if heroes[hero_name][0] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")

    elif action == "Recharge":
        hero_name = data[1]
        amount = int(data[2])

        if heroes[hero_name][1] + amount > 200:
            print(f"{hero_name} recharged for {200 - heroes[hero_name][1] } MP!")
            heroes[hero_name][1] = 200
        else:
            heroes[hero_name][1] += amount
            print(f"{hero_name} recharged for {amount} MP!")

    elif action == "Heal":
        hero_name = data[1]
        amount = int(data[2])

        if heroes[hero_name][0] + amount > 100:
            print(f"{hero_name} healed for {100 - heroes[hero_name][0] } HP!")
            heroes[hero_name][0] = 100
        else:
            heroes[hero_name][0] += amount
            print(f"{hero_name} healed for {amount} HP!")
    command = input()


heroes = dict(sorted(heroes.items(), key=lambda x: (-x[1][0], x[0])))

for key, value in heroes.items():
    print(key)
    print(f"HP: {value[0]}")
    print(f"MP: {value[1]}")








