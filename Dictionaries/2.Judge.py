# command = input()
#
# contests = {}
# individual_result = {}
#
# while command != "no more time":
#     data = command.split(" -> ")
#     user = data[0]
#     contest = data[1]
#     points = int(data[2])
#
#     if contest not in contests:
#         contests[contest] = []
#
#     is_true = False
#     for val in contests[contest]:
#         if user in val:
#             is_true = True
#             if val[1] < points:
#                 val[1] = points
#             break
#
#     if is_true == False:
#         contests[contest].append([user, points])
#     else:
#         pass
#
#     command = input()
#
#
# contests = dict(sorted(contests.items(), key=lambda x: (-len(x[1]), x[0])))
# counter = 1
# for key, value in contests.items():
#     counter = 1
#     print(f"{key}: {len(value)} participants")
#     for val in sorted(value, key=lambda x: x[1], reverse=True):
#         print(f"{counter}. {val[0]} <::> {val[1]}")
#         counter += 1
#
# counter = 1
# for key, value in contests.items():
#     for val in value:
#         if not val[0] in individual_result:
#             individual_result[val[0]] = val[1]
#         else:
#             individual_result[val[0]] += val[1]
#
# individual_result = dict(sorted(individual_result.items(), key=lambda x: ((-x[1]), x[0])))
#
# print("Individual standings:")
# for key, value in individual_result.items():
#     print(f"{counter}. {key} -> {value}")
#     counter += 1
#
#

submissions = {}
users = {}

while True:
    a = 5
    line = input()
    if line == "no more time":
        break
    line = line.split(" -> ")
    username = str(line[0])
    contest = str(line[1])
    points = int(line[2])

    if contest not in submissions:
        submissions[contest] = {username: points}
    if username not in submissions[contest]:
        submissions[contest][username] = points
    if username not in users:
        users[username] = {contest: points}
    else:
        users[username][contest] = points
    if submissions[contest][username] < points:
        submissions[contest][username] = points
    if users[username][contest] < points:
        users[username][contest] = points

for k, v in submissions.items():
    i = 1
    print(f'{k}: {len(v)} participants')
    sorted_items = dict(sorted(v.items(), key=lambda x: (-x[1], x[0])))
    for k2, v2 in sorted_items.items():
        print(f'{i}. {k2} <::> {v2}')
        i += 1
print('Individual standings:')
sorted_names = dict(sorted(users.items(), key=lambda x: (-sum(x[1].values()), x[0])))
i = 1
for k, v in sorted_names.items():
    print(f'{i}. {k} -> {sum(v.values())}')
    i += 1


print(submissions)