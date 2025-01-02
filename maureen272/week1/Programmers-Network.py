# programmers-lv3-dfs
def solution(n, computers):
    def dfs(node, visited):
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and visited[i] == False:
                dfs(i, visited) # 해당 노드를 방문한것으로 저장

    visited = [False] * n  # 방문 여부를 저장하는 리스트
    cnt = 0      # 네트워크 개수

    for i in range(n):
        if not visited[i]:  # 아직 방문하지 않은 컴퓨터에서 DFS 시작
            dfs(i, visited)
            cnt += 1  # 네트워크 개수 증가

    return cnt