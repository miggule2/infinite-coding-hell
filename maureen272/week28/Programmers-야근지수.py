import heapq

def solution(n, works):
    total = 0
    for w in works:
        total += w
    if total <= n: # 전체 작업량보다 퇴근시간까지 남은 시간이 더 많이 남으면 야근 피로도가 0임
        return 0
    
    heap = [-w for w in works] # heap은 최소heap 기준이기때문에 최대heap처럼 쓰기위해서 음수
    heapq.heapify(heap) # 최대힙 적용하기
    
    # n시간 동안 가장 큰 작업부터 1씩 줄이기
    for _ in range(n):
        max_work = -heapq.heappop(heap)
        if max_work == 0:
            heapq.heappush(heap, 0)
            break
        heapq.heappush(heap, -(max_work - 1))
        
    # 남은 작업량 계산
    ans = 0
    while heap:
        x = -heapq.heappop(heap)
        ans += x * x
    
    return ans