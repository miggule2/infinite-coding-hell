t = int(input())

def hap123(n):
    dp = [-1] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]

for i in range(t):
    n = int(input())
    print(hap123(n))