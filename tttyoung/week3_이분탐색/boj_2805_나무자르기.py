n, m = map(int, input().split())#나무의 갯수, 가져갈 총 길이
treelist = list(map(int, input().split()))

def binary_search(tree, M, start, end): #tree = treelist, M은 총 가져갈 나무의 길이의합, start시작길이 end끝나는 길이
    result = 0 #최종적으로 자를 길이
    while start<=end:
        mid = (start + end) // 2 #절단기 길이
        hap = 0
        for i in tree: #자르고 남은 합 구하기
            if i>mid: #자르는 길이가 나무 길이보다 짧으면 안 더함
                hap += (i - mid)

        if hap >= M: #자르고 남은 합이 가져갈 총 길이보다 크거나 작을경우(가져갈 길이로 딱 떨어지지 않을 경우도 있음, 문제에 "적어도"라고 되어있으므로 문제 잘 읽기!)
            result = mid #결과값에 일단 mid를 저장 후 이분탐색 이어가기, 만약 더 큰 값이 나올 경우 최댓값이 바뀜
            start = mid + 1
        else:
            end = mid - 1
    return result

print(binary_search(treelist, m, 0, max(treelist)))
