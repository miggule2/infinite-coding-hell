n = int(input())
list_n = list(map(int, input().split()[:n]))
m = int(input())
list_m = list(map(int, input().split()[:m]))

list_n.sort()
count = []

def binary_search(listn, M):
    start = 0
    end = len(listn) - 1

    while start <= end:
        mid = (start + end) // 2
        if M == listn[mid]:
            return 1 #있으면 1
        elif M > listn[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0 #없으면 0

for i in list_m:
    count.append(binary_search(list_n, i)) #지금까지 만든 1, 0 을 count리스트에 입력
print(' '.join(map(str, count))) #','없이 리스트를 출력