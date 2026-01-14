# 백준 1463번 - 1로 만들기
N = int(input())
dp = [0] * (N + 1) # 0~N까지의 수를 담을 dp테이블

for i in range(2, N + 1): # 2부터 N까지
    dp[i] = dp[i - 1] + 1 # 1을 빼는 경우 
    if i % 2 == 0: # 2로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i // 2] + 1) # 2로 나누는 경우
    if i % 3 == 0: # 3으로 나누어 떨어지는 경우
        dp[i] = min(dp[i], dp[i // 3] + 1) # 3으로 나누는 경우

print(dp[N])     
