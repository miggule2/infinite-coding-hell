def sel_sort(a):
    n = len(a)
    for i in range(0, n-1):#0부터 n-2까지 반복
        min_idx = i #최솟값의 위치
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j #j를 +1하면서 원래의 최솟값보다 작은 값이 있는지 찾는 과정, 찾으면 최솟값 index에 j를 넣음
        a[i], a[min_idx] = a[min_idx], a[i] #최솟값을 i번 위치바꿈
        print(a)

d = [2, 4, 3, 1, 6, 8, 0]
sel_sort(d)
print(d)