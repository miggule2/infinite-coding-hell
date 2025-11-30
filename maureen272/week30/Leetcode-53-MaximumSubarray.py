import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = -sys.maxsize
        sum = 0
        for num in nums:
            sum = max(num,sum+num)
            ans = max(ans, sum)

        return ans