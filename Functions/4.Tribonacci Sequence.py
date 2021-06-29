n = int(input())

def tribonacci(num):
    for number in range(1, n + 1):
        result = (num - 1) + (num - 2) + (num - 3)
        print(result)

tribonacci(n)