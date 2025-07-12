# BOJ - 16928 - 뱀과 사다리 게임

from collections import deque

n, m = map(int, input().split())
board = [i for i in range(101)]

# 사다리
for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

# 뱀
for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

visited = [False] * 101
queue = deque()
queue.append((1, 0))  # (현재 칸, 주사위 횟수)
visited[1] = True

while queue:
    now, cnt = queue.popleft()
    if now == 100:
        print(cnt)
        break
    for i in range(1, 7):
        next_pos = now + i
        if next_pos <= 100 and not visited[board[next_pos]]:
            visited[board[next_pos]] = True
            queue.append((board[next_pos], cnt + 1))
