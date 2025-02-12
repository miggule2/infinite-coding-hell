n = int(input())
bookdic = {}
for i in range(n):
    name = input()
    if name not in bookdic:
        bookdic[name] = 1
    else:
        bookdic[name] += 1

bookdic = dict(sorted(bookdic.items())) #사전순으로 미리 정렬
print(max(bookdic, key=bookdic.get)) #최대 value값을 가지는 key값을 추출

'''
n = int(input())
bookdic = {}
for i in range(n):
    name = input()
    if name not in bookdic:
        bookdic[name] = 1
    else:
        bookdic[name] += 1

max = max(bookdic.values())
list = []
for i in bookdic:
    if bookdic[i] == max:
        list.append(i)
list.sort()
print(list[0])
'''