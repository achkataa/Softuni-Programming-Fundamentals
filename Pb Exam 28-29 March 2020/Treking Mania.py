groups_number = int(input())
all_people = 0
musala_group = 0
monblan_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0
for group in range(1, groups_number + 1):
    people = int(input())
    all_people += people
    if people <= 5:
        musala_group += people
    elif people >= 6 and people <= 12:
        monblan_group += people
    elif people >= 13 and people <= 25:
        kilimandjaro_group += people
    elif people >= 26 and people <= 40:
        k2_group += people
    elif people >= 41:
        everest_group += people

print(f"{musala_group / all_people * 100:.2f}%")
print(f"{monblan_group / all_people * 100:.2f}%")
print(f"{kilimandjaro_group / all_people * 100:.2f}%")
print(f"{k2_group / all_people * 100:.2f}%")
print(f"{everest_group / all_people * 100:.2f}%")



