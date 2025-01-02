# programmers-lv3-dp
def solution(triangle):
    n = len(triangle)
    dp = [row[:] for row in triangle]

    # 아래에서 위로 DP 계산
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] += max(dp[i + 1][j], dp[i + 1][j + 1])

    return dp[0][0]