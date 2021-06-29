substrings = [substring for substring in input().split(", ")]
words = [word for word in input().split(", ")]

result_repeat = [sub for sub in substrings for word in words if sub in word]

for word in result_repeat:
    result_repeat = list(dict.fromkeys(result_repeat))

print(result_repeat)






