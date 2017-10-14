def simpleArraySum(n, ar):
    total = 0
    n -= 1

    while n >= 0:
        total += ar[n]
        n -= 1

    return total


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = simpleArraySum(n, ar)
print(result)
