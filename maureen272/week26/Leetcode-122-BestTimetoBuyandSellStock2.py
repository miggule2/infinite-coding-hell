class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = sum(max(prices[i] - prices[i-1], 0) for i in range(1, len(prices)-1))
        return result
    '''
    def maxProfit(self, prices):
        result = 0
        # 값이 오르는 경우 그리디로 계산
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                result += prices[i+1] - prices[i]
        return result
    '''