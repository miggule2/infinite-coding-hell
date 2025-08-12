import sys, heapq

input = sys.stdin.readline
M = int(input().strip())
N = int(input().strip())
coins = list(map(int, input().split()))

# 중복 제거 (불필요한 완화 줄이기)
coins = sorted(set(coins))
m = max(coins)

INF = 10**30
dist = [INF] * m
dist[0] = 0
hq = [(0, 0)]  # (비용 W, residue)

# 다익스트라: 엣지 가중치 = m - a, 이동: r -> (r + a) % m
while hq:
    d, r = heapq.heappop(hq)
    if d != dist[r]:
        continue
    for a in coins:
        nr = r + a
        if nr >= m:
            nr -= m
        nd = d + (m - a)
        if nd < dist[nr]:
            dist[nr] = nd
            heapq.heappush(hq, (nd, nr))

r = M % m
ans = (M + dist[r]) // m
print(ans)
