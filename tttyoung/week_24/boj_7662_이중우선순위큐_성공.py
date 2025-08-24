import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    min_heap = [] #최솟값 힙
    max_heap = [] #최댓값 힙
    k = int(input())
    visited = [False] * k #방문기록 생성 default fasle로 설정
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I': #입력값 최소,최대힙에 각각 push
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True #방문기록에 값이 있음을 표시
        else:
            if num == 1: #최댓값 힙일때 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]: #최소힙에서 지운걸 최대힙에서도 똑같이 동기화시켜주기 위해 삭제처리
                    heapq.heappop(max_heap)
                if max_heap: #실질적으로 현재 커맨드 수행
                    visited[max_heap[0][1]] = False #방문기록에서 삭제처리
                    heapq.heappop(max_heap)
            else: #최솟값 힙일때 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]: #최대힙에서 지운걸 최소힙에서도 똑같이 동기화시켜주기 위해 삭제처리
                    heapq.heappop(min_heap)
                if min_heap: #실질적으로 현재 커맨드 수행
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]: #마지막 삭제처리
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

                    
    if len(min_heap) == 0:
        print('EMPTY')
    else:
        print(-heapq.heappop(max_heap)[0], heapq.heappop(min_heap)[0])
