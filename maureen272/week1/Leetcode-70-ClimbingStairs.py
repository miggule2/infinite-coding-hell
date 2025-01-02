#처음에는 재귀로 풀었으나 timeout이 발생하여 memoization을 사용하여 풂
#Leetcode-level 1
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = collections.defaultdict(int)
        def climbStairs(self, n):
            if n <=2:
                return n
            
            if self.dp[n]:
                return self.dp[n]
            self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return self.dp[n]