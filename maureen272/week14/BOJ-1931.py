#BOJ 1931: 회의실 배정
import sys
input = sys.stdin.readline

n = int(input()) # 회의 개수
meetings = [tuple(map(int, input().split())) for _ in range(n)] # (시작시간, 끝나는시간)

meetings.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간 기준으로 정렬, 끝나는 시간이 같으면 시작시간 기준으로 정렬

end_time = 0 # 마지막 회의 끝나는 시간
count = 0 # 회의 개수

# 회의 개수 세기



for start, end in meetings: 
    if start >= end_time: # 시작시간이 마지막 회의 끝나는 시간보다 크거나 같으면 회의 가능
        end_time = end # 끝나는 시간 갱신
        count += 1 # 회의 개수 증가

print(count)