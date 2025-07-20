def tiling(n):
    dp = [0 for _ in range(n+2)]
    dp[1] = 1

    for i in range(2, n+1):
        if i%2 == 0: #홀수 짝수 경우를 나눠서 점화식 계산
            dp[i] = dp[i-1]*2 + 1
        else:
            dp[i] = dp[i-1]*2 - 1
    return dp[n]

n = int(input())
print(tiling(n)%10007)