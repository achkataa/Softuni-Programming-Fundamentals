# command = input()
# my_dict = {}
#
# while command != "End":
#     data = command.split(" -> ")
#     company_name = data[0]
#     id = data[1]
#
#     if not company_name in my_dict:
#         my_dict[company_name] = [id]
#     else:
#         if not id in my_dict[company_name]:
#             my_dict[company_name].append(id)
#     command = input()
#
#
# for key in sorted(my_dict, key=lambda x: x[0]):
#     print(f"{key}")
#     for val in sorted(my_dict[key]):
#         print(f"-- {val}")
#

command = input()

my_dict = {}

while command != "End":
    data = command.split(" -> ")
    company_name = data[0]
    employee_id = data[1]

    if company_name not in my_dict:
        my_dict[company_name] = []

    if employee_id not in my_dict[company_name]:
        my_dict[company_name].append(employee_id)


    command = input()

for key, value in sorted(my_dict.items(), key=lambda x: x[0]):
    print(f"{key}")
    for val in sorted(value):
        print(f"-- {val}")