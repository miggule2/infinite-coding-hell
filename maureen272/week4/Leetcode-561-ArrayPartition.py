class Solution(object):
    #solution1 : 파이썬다운 방식
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
    
    #solution2: 오름차순 풀이
    def arrayPairSum(self, nums):
        sum = 0
        pair = []
        nums.sort() #오름차순 정렬

        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                sum += min(pair)
                pair = []
        return sum