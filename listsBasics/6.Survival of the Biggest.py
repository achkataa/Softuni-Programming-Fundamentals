numbers = input().split()
n = int(input())
for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

for cycle in range(1, n + 1):
    numbers.remove(min(numbers))

print(numbers)