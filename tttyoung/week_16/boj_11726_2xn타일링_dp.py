def tiling(n):
    memo = [0] * (n+2) #memo[2]를 밑에서 따로 만들어주기때문에 1이 들어갔을때 n+1의 크기로 하면 인덱스 에러 발생, 
    #1을 예외처리로 두거나 memo리스트의 범위를 늘려주면 됨
    memo[1] = 1
    memo[2] = 2
    for i in range(3, n+1):
        memo[i] = (memo[i-1] + memo[i-2]) %10007 #그림 그려보면 i-1에는 가로 1칸짜리, i-2에는 가로 2칸짜리를 추가하면 된다. 
    return memo[n]

n = int(input())
print(tiling(n))


