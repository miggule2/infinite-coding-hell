import heapq

def solution(n, works):
    works = [-work for work in works]
    heapq.heapify(works)
    
    for i in range(n):
        # 작업량이 가장 큰 것
        if works:
            max_work = heapq.heappop(works)
            if max_work < 0:  # 작업량이 남아 있을 때만 감소
                max_work += 1
                heapq.heappush(works, max_work)
    result = sum(work ** 2 for work in works)
    # 남은 작업량으로 야근 피로도 계산
    return result