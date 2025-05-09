def make_one(n):
    memo = [-1] * (n+2)
    memo[1] = 0
    for i in range(2, n+1): #2,3은 기본값으로 주고 for문을 4부터 시작하려고 했지만 입력으로 1이 들아오면 indexerror가 발생.
        memo[i] = memo[i-1] + 1
        if i % 3 == 0: #3으로 나눠진다면 3으로 나눈 값과 i-1의 값 중 더 작은 값으로 넘어감.
            memo[i] = min(memo[i//3], memo[i]-1) + 1
        if i % 2 == 0: #2로 나눠진다면 2로 나눈값과 i-1의 값 중 더 작은 값으로 넘어감.
            #3으로 나눈 값보다 2로 나눈 값의 리턴값이 큰 경우를 고려하여 elif 대신 if를 써야함.
            memo[i] = min(memo[i//2], memo[i]-1) + 1 
    return memo[n]

N = int(input())
print(make_one(N))

