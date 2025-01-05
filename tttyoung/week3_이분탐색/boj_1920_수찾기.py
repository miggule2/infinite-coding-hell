n = int(input())
list_n = sorted(list(map(int, input().split()[:n])))
m = int(input())
list_m = list(map(int, input().split()[:m]))

def binary_search(listn, M):
    start = 0
    end = len(listn) - 1
    while start <= end:
        mid = (start + end) // 2
        if listn[mid] == M:
            return 1
        elif listn[mid] < M:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for i in list_m:
    print(binary_search(list_n, i))

