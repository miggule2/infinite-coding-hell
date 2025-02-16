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

#다른방법 풀이: get을 사용하지 않고 최대값을 찾은 후에 그 최댓값을 value로 가지는 모든 key값들을 list에 넣고 사전순으로 정렬하여 0번째 요소를 print
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