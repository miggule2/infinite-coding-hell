n, m = map(int, input().split())
dic_n = {}

for i in range(n):
    a = input()
    dic_n[a] = 1

for i in range(m):
    a = input()
    if a in dic_n:
        dic_n[a] += 1
    else: 
        dic_n[a] = 1

result = sorted([k for k, v in dic_n.items() if v == 2]) #value값으로 key값 찾기
print(len(result))
for i in result:
    print(i)