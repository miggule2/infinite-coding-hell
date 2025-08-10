import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

INF = 10**18
dist = [INF] * (V + 1)
dist[K] = 0
hq = [(0, K)]  # (현재까지 비용, 정점)

while hq:
    d, u = heapq.heappop(hq)
    if d != dist[u]:
        continue
    for v, w in graph[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(hq, (nd, v))

out = []
for i in range(1, V + 1):
    out.append(str(dist[i]) if dist[i] < INF else "INF")
print("\n".join(out))
