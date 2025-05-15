from collections import deque  

n, m = map(int, input().split())  # 미로의 크기 입력받기 (n: 세로, m: 가로)
maze = [list(map(int, list(input()))) for _ in range(n)]  # 각 줄은 문자열 -> 문자 하나하나를 정수로 변환하여 2차원 리스트로 저장

dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우 방향으로 이동할 때 x좌표의 변화량
dy = [0, 0, -1, 1]  # 상, 하, 좌, 우 방향으로 이동할 때 y좌표의 변화량

def bfs(x, y):  # 시작 위치는 (x, y)
    queue = deque()  # BFS에 사용할 큐를 생성
    queue.append((x, y))  # 시작 위치를 큐에 추가

    while queue:  # 큐가 빌 때까지 반복
        x, y = queue.popleft()  # 큐의 맨 앞에서 좌표를 꺼냄
        for i in range(4):  # 상, 하, 좌, 우 를 검사
            nx, ny = x + dx[i], y + dy[i]  # 이동한 후의 새로운 좌표 계산

            # 새로운 좌표가 미로 범위 안에 있고, 이동 가능한 칸(1)인 경우
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1  # 현재 칸까지의 거리 +1을 저장하여 이동 횟수를 기록
                queue.append((nx, ny))  # 다음 탐색 대상으로 큐에 추가

# (0, 0)에서 BFS를 시작
bfs(0, 0)

# 도착지점 (n-1, m-1)까지의 최소 칸 수 출력
print(maze[n - 1][m - 1])
