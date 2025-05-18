import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y, color, board, visited, N):
    visited[x][y] = True
    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and board[nx][ny] == color:
                dfs(nx, ny, color, board, visited, N)

def count_regions(board, N):
    visited = [[False]*N for _ in range(N)]
    regions = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                dfs(i, j, board[i][j], board, visited, N)
                regions += 1
    return regions

def main():
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]
    
    normal_cnt = count_regions(board, N)
    
    cb_board = [row.copy() for row in board]
    for i in range(N):
        for j in range(N):
            if cb_board[i][j] == 'G':
                cb_board[i][j] = 'R'
    
    cb_cnt = count_regions(cb_board, N)
    
    print(normal_cnt, cb_cnt)

if __name__ == "__main__":
    main()
