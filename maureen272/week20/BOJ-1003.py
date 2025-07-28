# 백준 1003 - 피보나치 함수
T = int(input())
cases = [int(input()) for _ in range(T)]

# 최대 N은 40(문제에서 주어짐)
dp = [[0, 0] for _ in range(41)]

# 초기 조건
dp[0] = [1, 0]  # fibonacci(0): 0이 1번, 1이 0번 출력
dp[1] = [0, 1]  # fibonacci(1): 0이 0번, 1이 1번 출력

# dp를 이용하여 피보나치 함수의 호출 횟수 계산
for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0] # 0의 호출 횟수
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1] # 1의 호출 횟수

# 각 테스트케이스에 대해 출력
for n in cases:
    print(dp[n][0], dp[n][1])
