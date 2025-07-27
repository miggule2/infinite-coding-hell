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
            print(hq.heappop(heap)[1]) 
    else:
        hq.heappush(heap, (abs(x), x)) #heap에 저장할때 튜플로 저장