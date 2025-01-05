#이분탐색

def binary_search(a, x): #a는 리스트, x찾는값
    start = 0
    end = len(a) - 1 #리스트 마지막값 index

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return -1
d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))
