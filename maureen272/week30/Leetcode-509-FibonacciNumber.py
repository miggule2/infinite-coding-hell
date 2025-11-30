import collections
class Solution(object):
    dp = collections.defaultdict(int) # 기본값이 0인 딕셔너리 생성

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <= 1:
        #     return n
        # return self.fib(n-1) + self.fib(n-2)
        #-------------------------------------------------------------------
        # if n <= 1: # base case : n이 0 또는 1인 경우
        #     return n
    
        # if self.dp[n] : # 이미 계산된 값이 있는 경우
        #     return self.dp[n] # 저장된 값 반환
        
        # self.dp[n] = self.fib(n-1) + self.fib(n-2) # 메모이제이션: 계산된 값을 저장
        # return self.dp[n] # 계산된 값 반환
        #------------------------------------------------------------------------
        self.dp[1] = 1 # 초기값 설정
        for i in range(2, n + 1): # 2부터 n까지 반복
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2] # 점화식
        return self.dp[n] # 최종 결과 반환