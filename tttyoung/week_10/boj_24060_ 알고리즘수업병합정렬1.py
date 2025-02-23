def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2  # 중간 지점 계산
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

def merge(A, p, q, r):
    global cnt, result
    tmp = []  # 임시 배열
    i, j = p, q + 1  # 두 부분 리스트의 시작점

    # 두 부분 리스트를 병합
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1

    # 왼쪽 배열의 남은 요소 추가
    while i <= q:
        tmp.append(A[i])
        i += 1

    # 오른쪽 배열의 남은 요소 추가
    while j <= r:
        tmp.append(A[j])
        j += 1

    # 정렬된 결과를 원래 리스트에 반영
    t = 0
    for k in range(p, r + 1):
        A[k] = tmp[t]
        cnt += 1
        result.append(tmp[t])
        t += 1
    
cnt = 0
result = []

a, k = map(int, input().split())
arr = list(map(int, input().split()))

merge_sort(arr, 0, len(arr) - 1)
if k > cnt:
    print(-1)
else:
    print(result[k-1])




