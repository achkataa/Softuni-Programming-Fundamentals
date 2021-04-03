shards = 0
motes = 0
fragments = 0
LINE = 250
counter = 0

normal_items = {}
special_items = {"shards": 0, "motes": 0, "fragments": 0}
result = []
total = {}
flipped = {}

while shards < LINE and motes < LINE and fragments < LINE:
    materials = [mat for mat in input().split()]
    for material in range(1, len(materials), 2):
        key = materials[material].lower()
        value = int(materials[material - 1])

        if key == "shards" or key == "motes" or key == "fragments":
            special_items[key] += value
            if key == "shards":
                shards += value
                if shards >= LINE:
                    print("Shadowmourne obtained!")
                    break
            elif key == "motes":
                motes += value
                if motes >= LINE:
                    print("Dragonwrath obtained!")
                    break
            elif key == "fragments":
                fragments += value
                if fragments >= LINE:
                    print("Valanyr obtained!")
                    break
        else:
            if key in special_items:
                normal_items[key] += value
            else:
                normal_items[key] = value

for key, value in special_items.items():
    if value >= LINE:
        special_items[key] -= LINE


for key, value in special_items.items():
    if not value in result:
        result.append(value)
        counter += 1


a = sorted(special_items.items(), key=lambda x: x[1])
for key, value in sorted(dict(a).items(), key=lambda x: x[1], reverse=True):
    total[key] = value

for key, value in total.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)

for key, value in flipped.items():
    value = sorted(value)
    for v in value:
        print(f"{v}: {key}")








for key, value in sorted(normal_items.items(), key=lambda kv: kv[0]):
    print(f"{key}: {value}")











