# BOJ - 11053 - 가장 긴 증가하는 부분 수열
N = int(input())  
A = list(map(int, input().split()))  

dp = [1] * N  # 각 원소를 포함하는 가장 긴 증가하는 부분 수열의 길이

for i in range(1, N): # i는 1부터 N-1까지
    for j in range(i): # j는 0부터 i-1까지
        if A[i] > A[j]: # A[i]가 A[j]보다 클 때
            dp[i] = max(dp[i], dp[j] + 1) # dp[i]를 업데이트

print(max(dp)) # 가장 긴 증가하는 부분 수열의 길이 출력