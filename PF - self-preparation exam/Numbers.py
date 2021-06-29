numbers = [int(num) for num in input().split()]

average = sum(numbers) / len(numbers)

greater_than_average = [num for num in numbers if num > average]

greater_than_average = sorted(greater_than_average, reverse=True)

if not greater_than_average:
    print("No")
elif len(greater_than_average) <= 5:
    print(' '.join(str(num) for num in greater_than_average))
else:
    for n in range(5):
        print(greater_than_average[n], end=" ")

