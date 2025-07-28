import heapq as hq #heap 모듈사용
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else: #변환된 최댓값을 다시 원래 형태로 변환
            print(-hq.heappop(heap)) #추출할때는 앞에 다시 -를 붙임
    else: #heap모듈은 최솟값만 지원해주기 때문에 음수부호를 붙여 최댓값을 최솟값으로 변환
        hq.heappush(heap, -x) #heap에 -x저장