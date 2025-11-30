from collections import deque
n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))

#좌표이동 변수
dx = [1, -1, 0, 0] 
dy = [0, 0, -1, 1]

def bfs_maze(x, y):
    qu = deque()
    qu.append((x, y))

    while qu:
        x, y = qu.popleft()
        for i in range(4): #상하좌우 확인하는 과정
            nx, ny = x + dx[i], y + dy[i] #이동한 거리만큼 더함.
            #지나가게 되는 길일때(1일때) 이전 값에 1을 더해서 visited없이 자체적으로 방문기록 표현되면서 거리계산도 됨.
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1: 
                qu.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1

    return maze[n-1][m-1] 

print(bfs_maze(0, 0))
