# 12851 숨바꼭질 2
from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [0] * MAX
    ways = [0] * MAX  # 각 위치까지 최단 시간으로 도달하는 방법 수 저장

    queue = deque()
    queue.append(n)
    visited[n] = 1  # 시작점 방문 처리 (시간 0 대신 1로 저장해서 -1 연산 안 해도 되게)

    while queue:
        cur = queue.popleft()
        for next_pos in [cur - 1, cur + 1, cur * 2]:
            if 0 <= next_pos < MAX:
                # 처음 방문하는 경우
                if visited[next_pos] == 0:
                    visited[next_pos] = visited[cur] + 1
                    ways[next_pos] = ways[cur] if ways[cur] > 0 else 1
                    queue.append(next_pos)
                # 이미 방문했지만, 같은 시간에 도달 가능한 경우
                elif visited[next_pos] == visited[cur] + 1:
                    ways[next_pos] += ways[cur] if ways[cur] > 0 else 1

    return visited[k] - 1, ways[k] if ways[k] > 0 else 1  # 시간은 1 빼고, 방법 수가 0이면 1로

# 입력
n, k = map(int, input().split())
time, count = bfs(n, k)

# 출력
print(time)
print(count)
