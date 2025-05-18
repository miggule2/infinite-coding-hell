import sys
input = sys.stdin.readline

MAX_N = 40
count0 = [0] * (MAX_N + 1)
count1 = [0] * (MAX_N + 1)

count0[0], count1[0] = 1, 0
count0[1], count1[1] = 0, 1

for n in range(2, MAX_N + 1):
    count0[n] = count0[n-1] + count0[n-2]
    count1[n] = count1[n-1] + count1[n-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(count0[N], count1[N])
