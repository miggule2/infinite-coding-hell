from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[0] * m for _ in range(n)] #방문기록
    oil_sizes = {}     
    chunk_id = 1

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                q = deque([(i, j)])
                visited[i][j] = chunk_id
                count = 1
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = x + dx, y + dy
                        #범위 내에 있으면서 석유가 있고 방문하지 않은 곳일때
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == 0: 
                            visited[nx][ny] = chunk_id
                            q.append((nx, ny))
                            count += 1
                
                oil_sizes[chunk_id] = count
                chunk_id += 1
    #열 기준으로 돌면서 최대 석유량 계산
    max_oil = 0
    for j in range(m):
        seen_chunks = set() #중복제거
        for i in range(n):
            if visited[i][j] > 0:
                seen_chunks.add(visited[i][j]) 
        #현재 열 총 석유량 계산
        current_oil = sum(oil_sizes[id] for id in seen_chunks)
        max_oil = max(max_oil, current_oil)
        
    return max_oil