# 백준 9461번 -  파도반 수열
T = int(input())

# 파도반 수열 초기값
P = [0] * 101
P[1], P[2], P[3] = 1, 1, 1

# 점화식: P(n) = P(n-2) + P(n-3)
for i in range(4, 101):
    P[i] = P[i - 2] + P[i - 3]

for _ in range(T):
    N = int(input())
    print(P[N])
