import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    min_heap = [] #최솟값 힙
    max_heap = [] #최댓값 힙
    k = int(input())
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I': #입력값 최소,최대힙에 각각 push
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num == 1: #최댓값 힙일때 최댓값 삭제
                x = -heapq.heappop(max_heap)
                min_heap.remove(x) #같은 값을 최솟값 힙에서도 삭제
                heapq.heapify(min_heap)
            else: #최솟값 힙일때 최솟값 삭제
                x = heapq.heappop(min_heap)
                max_heap.remove(-x) #같은값을 최댓값 힙에서도 삭제
                heapq.heapify(max_heap)
                    
    if len(min_heap) == 0:
        print('EMPTY')
    else:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))