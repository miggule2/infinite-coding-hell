n, m = map(int, input().split())
id_dic = {}
for i in range(n):
    a, b = map(str, input().split())
    id_dic[a] = b

for i in range(m):
    id = input()
    print(id_dic[id])
