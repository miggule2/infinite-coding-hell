#이분탐색

def binary_search_sub(a, x, start, end): #a는 리스트, x찾는값
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_sub(a, x, mid + 1, end)
    else:
        return binary_search_sub(a, x, start, mid-1)
    
    return -1

def binary_search(a, x):
    return binary_search_sub(a, x, 0, len(a)-1)

    


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))
