def rope(n, r_list):
    max_list = []
    for i in range(n):
        #내림차순 정렬상으로 k개의 로프를 사용한다고 할때 가장 작은 로프 무게는 r_list의 k번째 index에 위치
        max_list.append(r_list[i]*(i+1)) #가장 작은 로프무게 기준으로 로프 개수별 최대값 구하기
    return max(max_list)


n = int(input())
r_list = [int(input()) for _ in range(n)]
r_list.sort(reverse=True) #큰 값이 먼저오도록 내림차순정렬

print(rope(n, r_list))

