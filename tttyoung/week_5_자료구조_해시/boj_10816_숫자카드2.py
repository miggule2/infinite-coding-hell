def binary(dic_h, h, x): #dic_h는 딕셔너리, h는 그 딕셔너리를 리스트화시킨것, x는 찾고자하는 숫자
    start = 0
    end = len(h) - 1

    while start<=end:
        mid = (start + end) // 2
        if h[mid] == x:
            return dic_h[x]
        elif h[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
list_n = list(map(int, input().split()[:n]))
m = int(input())
list_m = list(map(int, input().split()[:m]))
list_n.sort()

hash = {}
result = []
for i in list_n: #list_n을 딕셔너리로 나타내어 숫자는 key, 갯수는 value로 나타냄
    if i in hash:
        hash[i] += 1
    else:
        hash[i] = 1

list_hash = [*hash.keys()] #딕셔너리 hash를 리스트화

for i in list_m:
    result.append(binary(hash, list_hash, i))
print(' '.join(map(str, result)))
    
