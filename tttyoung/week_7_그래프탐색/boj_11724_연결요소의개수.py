node, edge = map(int, input().split())
edgelist = []

for i in range(edge):
    e = list(map(int, input().split()))
    edgelist.append(e)

def change(edgelist, node): #간선목록을 인접리스트(딕셔너리)로 바꿔주는 함수
    edgedic= {}
    for i in range(node):
        edgedic[i+1] = []
    for a, b in edgelist:
        if a in edgedic:
            edgedic[a].append(b)
        if b in edgedic:
            edgedic[b].append(a)
    return edgedic

def bfs(edgedic, start, done):#done을 이용해 재귀를 하기 위해서 매개변수로 위치함.
    qu = []
    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        for num in edgedic[p]:
            if num not in done:
                qu.append(num)
                done.add(num)

count = 0
done = set()
edgedic = change(edgelist, node)

for i in range(1, node + 1): #연결요소 개수 세기위한 함수, 1부터 n까지의 노드 개수만큼 for문을 반복하여 노드가 done에 없으면 재귀해서 연결요소묶음 찾기. 이미 연결한 묶음의 요소들은 모두 done에 추가되어있음.
    if i not in done:
        bfs(edgedic, i, done)
        count += 1

print(count)








