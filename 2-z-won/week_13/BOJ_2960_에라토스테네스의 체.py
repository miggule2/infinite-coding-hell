import sys
input = sys.stdin.readline

N, K = map(int, input().split())
is_removed = [False] * (N + 1)
count = 0

for i in range(2, N + 1):
    if not is_removed[i]:
        is_removed[i] = True
        count += 1
        if count == K:
            print(i)
            break
        for j in range(i * 2, N + 1, i):
            if not is_removed[j]:
                is_removed[j] = True
                count += 1
                if count == K:
                    print(j)
                    sys.exit(0)
