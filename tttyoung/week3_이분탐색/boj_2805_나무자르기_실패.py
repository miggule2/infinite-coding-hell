n, m = map(int, input().split())#나무의 갯수, 가져갈 총 길이
treelist = list(map(int, input().split()))

def binary_search(tree, M, start, end): #tree = treelist, M은 총 가져갈 나무의 길이의합, start시작길이 end끝나는 길이
    while start<=end:
        mid = (start + end) // 2 #절단기 길이
        hap = 0
        for i in tree:     
            if i>mid:
                hap += (i - mid)

        if M == hap: 
            return mid 
        elif M < hap:
            start = mid + 1
        else: 
            end = mid - 1

print(binary_search(treelist, m, 0, max(treelist)))
     