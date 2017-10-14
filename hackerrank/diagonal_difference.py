def addColumns(n, a):
    cell = 0

    total1 = 0
    while cell < n:
        total1 += a[cell][cell]
        cell += 1

    total2 = 0
    row = 0
    cell = n - 1
    while cell >= 0:
        total2 += a[row][cell]
        row += 1
        cell -= 1

    return abs(total1 - total2)


n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

result = addColumns(n, a)
print(result)
