import heapq as hq 
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for i in range(n):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-hq.heappop(heap)) #추출할때는 앞에 다시 -를 붙임
    else:
        hq.heappush(heap, -x) #heap에 -x저장