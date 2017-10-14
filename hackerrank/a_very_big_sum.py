"""
5
1000000001 1000000002 1000000003 1000000004 1000000005
"""


def aVeryBigSum(n, ar):
    n -= 1

    total = 0
    while n >= 0:
        total += ar[n]
        n -= 1
    return total


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = aVeryBigSum(n, ar)
print(result)
