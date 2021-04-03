my_dict = {"A": [1,2,3], "B": [4,5,6], "C": [7,8,9], "D": [10,11,12]}


for value in my_dict.values():
    if 1 in value:
        print(True)
    else:
        print(False)