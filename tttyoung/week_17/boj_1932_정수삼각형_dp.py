def int_tri(n, tri_list):
    dp = [[0]*(i+1)for i in range(n)]
    dp[n-1] = tri_list[n-1]
    for i in range(n-2,-1,-1):#입력된 정수리스트를 거꾸로 시작하여 마지막에 가장 윗값이 오도록 for문 구현
        for j in range(i+1):
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + tri_list[i][j]#해당칸의 값은 다음줄 같은위치와 다음줄 다음 위치값중 큰 값
    return dp[0][0]

n = int(input())
tri_list = [list(map(int, input().split())) for _ in range(n)]
print(int_tri(n, tri_list))
