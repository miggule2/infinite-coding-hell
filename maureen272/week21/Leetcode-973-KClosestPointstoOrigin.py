class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        lst = [] # 빈 리스트 생성
        for (x,y) in points: # 각 점에 대해 거리 계산
            distance = x**2 + y**2 # 유클리드 거리의 제곱
            lst.append((distance, x, y)) # 거리와 좌표를 튜플로 저장
        lst.sort() # 리스트 정렬 (거리 기준)
        return [[x, y] for (_, x, y) in lst[:k]] # k개의 가장 가까운 점 반환