n = int(input())
l = list()
for _ in range(n):
    l.append(int(input()))

l.sort()
for i in l:
    print(i)