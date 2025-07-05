# BOJ - 1167 - 트리의 지름
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V = int(input()) # 노드의 개수
graph = [[] for _ in range(V + 1)] # 그래프 초기화

# 그래프 구성
for _ in range(V):
    data = list(map(int, input().split())) # 각 노드와 연결된 노드, 가중치 정보 입력
    node = data[0] 
    for i in range(1, len(data) - 1, 2): 
        next_node = data[i]  # 연결된 노드
        weight = data[i + 1] # 가중치
        graph[node].append((next_node, weight))  # 연결된 노드와 가중치 추가

# DFS
def dfs(node, dist):
    global max_dist, far_node
    visited[node] = True
    if dist > max_dist:
        max_dist = dist
        far_node = node
    for next_node, weight in graph[node]:
        if not visited[next_node]:
            dfs(next_node, dist + weight)

# 첫 번째 DFS: 임의의 노드(1번)에서 가장 먼 노드 찾기
visited = [False] * (V + 1)
max_dist = 0
far_node = 0
dfs(1, 0)

# 두 번째 DFS: 가장 먼 노드에서 다시 DFS하여 지름 구하기
visited = [False] * (V + 1)
max_dist = 0
dfs(far_node, 0)

print(max_dist)
