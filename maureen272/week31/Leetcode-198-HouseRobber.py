import collections

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: # list가 비어있는 경우 0을 리턴
            return 0
        if len(nums) <=2: # list의 길이가 2이하인 경우 가장 큰 값을 리턴
            return max(nums)
        
        dp = collections.OrderedDict() # orderedDict는 입력된 순서를 유지하는 딕셔너리
        dp[0], dp[1] = nums[0], max(nums[0],nums[1]) # dp[0]은 첫번째 집의 금액, dp[1]은 첫번째 집과 두번째 집 중 큰 금액
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i]) # 현재 집을 털지 않는 경우(dp[i-1])와 현재 집을 터는 경우(dp[i-2] + nums[i]) 중 큰 금액 저장

        return dp.popitem()[1] # 마지막 집까지의 최대 금액
