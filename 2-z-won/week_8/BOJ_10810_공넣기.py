m, n = map(int, input().split())
bagooni = [0] * m
for _ in range(n):
    i, j, k = map(int, input().split())
    for l in range(i, j+1, 1):
        bagooni[l-1] = k
for u in bagooni:
    print(u, end=" ")
print()