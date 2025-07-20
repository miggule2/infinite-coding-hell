def tri_sequence(n):
    dp = [0] * max(n, 5) #n과 5중 더 큰 값을 선택하여 리스트의 크기를 결정함. 리스트의 크기는 무조건 5이상이 되어야하기 때문.  
    dp[0] = dp[1] = dp[2] = 1
    dp[3] = dp[4] = 2
    
    for i in range(5, n):
        dp[i] = dp[i-1] + dp[i-5]
    
    return dp[n-1] #입력 n은 index + 1이기 때문에 n-1번째 숫자를 구함

t = int(input())
for _ in range(t):
    n = int(input())
    print(tri_sequence(n))
