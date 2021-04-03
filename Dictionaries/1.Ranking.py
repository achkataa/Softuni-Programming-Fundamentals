contests = input()

contests_dict = {}
while contests != "end of contests":
    data = contests.split(":")
    contest_name = data[0]
    contest_password = data[1]

    contests_dict[contest_name] = [contest_password]

    contests = input()

submissions = input()
submissions_dict = {}

while submissions != "end of submissions":
    data = submissions.split("=>")
    contest_name = data[0]
    contest_password = data[1]
    username = data[2]
    points = int(data[3])

    if contest_name in contests_dict:
        if contest_password == contests_dict[contest_name]:
            contests_dict[contest_name].append([username, points])
    submissions = input()




