n = int(input())
list_n = list(map(int, input().split()[:n]))
m = int(input())
list_m = list(map(int, input().split()[:m]))

#리스트를 set으로 바꾼후 중복제거하여 다시 리스트로 만듦
set_n = set(list_n) 
sorted_set = sorted(set_n)
list_set = list(sorted_set)
countlist = []

def binary_search(setlistn, M):
    start = 0
    end = len(setlistn) - 1

    while start <= end:
        mid = (start + end) // 2
        if M == setlistn[mid]:
            return list_n.count(M) #값이 있다면 count함수를 사용하여 그 갯수를 return
        elif M > setlistn[mid]:
            start = mid + 1
        else:
            end = mid - 1

for i in list_m:
    countnum = binary_search(list_set, i) #count한 갯수를 변수에 넣음
    if countnum == None: #갯수가 없다면 None을 0으로 변환
        countnum = 0
    countlist.append(countnum) #countlist에 갯수를 넣음
    result = ' '.join(map(str, countlist)) #','를 제외한 리스트 출력
print(result)