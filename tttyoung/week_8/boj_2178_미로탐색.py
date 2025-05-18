from collections import deque
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

dx = [1, -1, 0, 0] #상하좌우로 하나씩 이동하는 변수, 이를 통해 상하좌우에 1이 있는지 0(벽)이 있는지 확인.
dy = [0, 0, -1, 1]

def bfs_maze(x, y):
    qu = deque()
    qu.append((x, y))

    while qu:
        x, y = qu.popleft()
        for i in range(4): #상하좌우 확인하는 과정
            nx, ny = x + dx[i], y + dy[i] #이동한 거리만큼 더함.
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1: #nx, ny가 미로 범위 안에 있으면서 그 좌표에 해당하는 칸이 1이라면 큐에 추가해주고 해당 칸에 1을 더하여 그 칸의 값을 거리로 알 수 있게 해줌.
                qu.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[n-1][m-1] 

print(bfs_maze(0, 0))
