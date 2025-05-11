def rgb(n, rgb_list):
    dp = [[0, 0, 0] for _ in range(n)]
    dp[0] = rgb_list[0] #for문 돌리기 위해 초기값 설정
    for i in range(1, n): #누적합을 이용하여 dp테이블 구현 
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + rgb_list[i][0] #빨강일때 이때까지의 최솟값+현재값
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + rgb_list[i][1] #초록일때 이때까지의 최솟값+현재값
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + rgb_list[i][2] #파랑일때 이때까지의 최솟값+현재값
    return min(dp[n-1]) #마지막 3가지색의 경우 중 가장 작은 경우를 출력

n = int(input())
rgb_list = [list(map(int, input().split())) for _ in range(n)]
print(rgb(n, rgb_list))
