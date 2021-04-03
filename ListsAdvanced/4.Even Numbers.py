numbers = list(map(lambda x: int(x), input().split(", ")))

even_numbers = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(even_numbers)




