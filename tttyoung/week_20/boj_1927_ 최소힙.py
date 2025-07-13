import heapq as hq #힙 사용을 위한 모듈
import sys
input = sys.stdin.readline

N = int(input())
heap = []
result = []

for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(hq.heappop(heap))
    else:
        hq.heappush(heap, x)