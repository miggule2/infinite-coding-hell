from collections import defaultdict 

n, m, v = map(int, input().split())
edgelist = []

for i in range(m):
    edgelist.append(list(map(int, input().split())))

def change(edgelist, n): #간선목록을 인접리스트(딕셔너리)로 바꿔주는 함수
    edgedic= {}
    for i in range(n): #start값이 어떠한 노드랑도 연결이 안되어있을 경우 keyerror가 남. 따라서 혼자 있는 노드도 비어있는 딕셔너리를 만들어줘야함.
        edgedic[i+1] = []
    for a, b in edgelist:
        if a in edgedic:
            edgedic[a].append(b)
        if b in edgedic:
            edgedic[b].append(a)
    return edgedic


def dfs_stack(edgedic, start):
    st = [start] #스택 초기화
    done = set()
    result = []

    while st:
        s = st.pop()
        if s not in done:
            done.add(s)
            result.append(s)
            st.extend(reversed(edgedic[s])) #스택에 이웃 노드 추가
    print(*result)

def bfs(edgedic, start):
    qu = []
    done = set()
    result = []

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        result.append(p)
        for i in edgedic[p]:
            if i not in done:
                qu.append(i)
                done.add(i)
    print(*result)
   
edgedic = change(edgelist, n)
for key in edgedic: #딕셔너리 밸류값들을 오름차순으로 정리함.
    edgedic[key].sort()

dfs_stack(edgedic, v)
bfs(edgedic, v)

