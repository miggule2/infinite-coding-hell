from collections import deque
n, m = map(int, input().split())
num = list(map(int, input().split()))
table = deque([_ for _ in range(1, n+1)])
count = 0

for i in num:
    while 1:
        if i == table[0]:
            table.popleft()
            break
        else:
            if table.index(i) <= len(table) - table.index(i):
                table.rotate(-1)
                count+=1

            elif table.index(i) > len(table) - table.index(i):
                table.rotate(1)
                count+=1  

print(count)