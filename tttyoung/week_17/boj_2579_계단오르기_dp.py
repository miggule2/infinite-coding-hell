def stair(n, s_list):
    dp = [0] * (n+1)
    dp[0] = s_list[0] #계단이 2칸 이하일 경우는 고정값
    if n>1:
        dp[1] = dp[0] + s_list[1]
    for i in range(2, n):
        dp[i] = max(dp[i-3] + s_list[i-1], dp[i-2]) + s_list[i] 
        #특정칸으로 가기 위한 과정은 n-2에서 2칸을 점프하거나 n-1에서 1칸 점프해서 오는 경우임.
        #n-1에서 1칸 점프에서 오기 위해서는 그 전에 위치했던 칸이 n-3이여야함.(3칸을 연속으로 점프할 수는 없기때문)
        #점화식을 구할때 경우가 나눠지는것을 분기점으로 점화식을 생각해야함함
    return dp[n-1]

n = int(input())
s_list = [int(input()) for _ in range(n)]
print(stair(n, s_list))
    