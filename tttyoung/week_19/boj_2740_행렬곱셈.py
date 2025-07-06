N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

C = [[0 for _ in range(K)] for _ in range(N)] #result행렬 0으로 세팅

#i, j가 고정일때 k값을 변동하면서 그 합을 누적하여 C[i][j]를 구함.
for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] *B[k][j]
            
#캐시 친화적 코드
#kij순서로 for문을 돌리면서 행마다 한번식 곱하여 누적하는 방식으로 기존의 ijk와 달리 C[i][j]를 하나씩 한번에 완성시키는것이 아닌, k for문이 돌때까지 행으로 분산하여 계산해주고 누적합을 통해 C를 완성시킴.
for k in range(M):
    for i in range(N):
        r = A[i][k]
        for j in range(K):
            C[i][j] += r *B[k][j]

for p in range(N):
    print(*C[p])