num = int(input())
strlist = []
for i in range(num):
    a = input()
    strlist.append(a)

strlist = list(set(strlist))
strlist.sort()
strlist.sort(key = len)

for i in range(len(strlist)):
    print(strlist[i])