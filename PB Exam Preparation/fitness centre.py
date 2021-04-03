visitors = int(input())
back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

training = 0
customers = 0



for visitor in range(1, visitors + 1):
    action = input()
    if action == "Back":
        back += 1
        training += 1
    elif action == "Chest":
        chest += 1
        training += 1
    elif action == "Legs":
        legs += 1
        training += 1
    elif action == "Abs":
        abs += 1
        training += 1
    elif action == "Protein shake":
        protein_shake += 1
        customers += 1
    elif action == "Protein bar":
        protein_bar += 1
        customers += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(training * 100) / visitors:.2f}% - work out")
print(f"{(customers * 100) / visitors:.2f}% - protein")




