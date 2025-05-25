n = int(input())
money, rate = map(int, input().split())
info = []
flag = 0
for _ in range(n):
    info_d = list(map(int, input().split()))
    info.append(info_d)
for i in info:
    if i[1] > rate:
        if money >= i[0]:
            print("YES")
            flag = 1
            break
if flag == 0:
    print("NO")