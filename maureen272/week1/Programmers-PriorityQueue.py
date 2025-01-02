# programmers-lv3-pq
import heapq

def solution(operations):
    min_heap = []  
    max_heap = [] 
    entry_finder = set()  # 현재 큐에 있는 유효한 값들

    for operation in operations:
        command, value = operation.split()
        value = int(value)

        if command == "I":
            heapq.heappush(min_heap, value)
            heapq.heappush(max_heap, -value)
            entry_finder.add(value)

        elif command == "D":
            #if not entry_finder: 
            #    continue
            #최댓값 제거
            if value == 1:  
                # invalid한 값 제거
                while max_heap and -max_heap[0] not in entry_finder:
                    heapq.heappop(max_heap)  
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_finder.remove(max_val)
            #최솟값 제거
            elif value == -1: 
                while min_heap and min_heap[0] not in entry_finder:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_finder.remove(min_val)

    while min_heap and min_heap[0] not in entry_finder:
        heapq.heappop(min_heap)
    while max_heap and -max_heap[0] not in entry_finder:
        heapq.heappop(max_heap)

    if not entry_finder:
        return [0, 0]

    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]