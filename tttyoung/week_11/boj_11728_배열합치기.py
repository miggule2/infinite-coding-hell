n, m = map(int, input().split())
listn = list(map(int, input().split()))
listm = list(map(int, input().split()))

for i in listm:
    listn.append(i)

listn.sort()
print(" ".join(map(str, listn)))