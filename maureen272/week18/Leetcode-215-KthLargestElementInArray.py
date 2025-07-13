import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = list()  # Min-heap을 사용하여 k번째로 큰 요소를 찾기 위한 힙 초기화
        for n in nums: # nums 리스트의 각 요소에 대해
            heapq.heappush(heap, -n) # 힙에 음수로 변환하여 추가 (최소 힙을 최대 힙처럼 사용)
            
        for i in range(1, k): # k번째 요소를 찾기 위해 k-1번 pop
            heapq.heappop(heap) # 가장 작은 요소를 제거 (음수로 저장되어 있으므로 실제로는 가장 큰 요소를 제거)
        return -heapq.heappop(heap) # k번째로 큰 요소를 반환 (음수로 저장되어 있으므로 다시 양수로 변환)