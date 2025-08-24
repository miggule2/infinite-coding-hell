class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums) # nums 배열에서 중복을 제거한 set을 만들고 set의 모든 요소를 더한 값에 2를 곱함(이 값은 배열의 모든 요소가 두 번씩 나타났을 때의 총합임)
                                              # 여기서 전체 합에서 중복된 요소의 합을 빼면 한 번만 나타나는 요소의 값이 남음

# 문제에서 의도한 풀이
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         result = 0
#         for num in nums:
#             result ^= num
#         return result