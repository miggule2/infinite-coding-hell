comnum = int(input())
netnum = int(input())
netlist = []
for i in range(netnum):
    net = list(map(int, input().split()))
    netlist.append(net)

def com_find(g, start): #bfs로 그래프 탐색
    qu = []
    done = set()
    count = 0

    qu.append(start)
    done.add(start)

    while qu:
        p = qu.pop(0)
        count += 1
        for num in g[p]:
            if num not in done:
                qu.append(num)
                done.add(num)
    return count - 1

def change(edge): #간선목록으로 입력 받은값을 인접리스트(딕셔너리)로 바꾸는 함수
    netdic = {}
    for a, b in edge:
        if a not in netdic:
            netdic[a] = []
        if b not in netdic:
            netdic[b] = []
        netdic[a].append(b)
        netdic[b].append(a)
    if 1 not in netdic: #만약 1번 컴퓨터가 어떤 컴퓨터와도 인접해있지 않으면 딕셔너리에 추가 자체가 안돼서 런타임에러가 발생함. 
        #만약 우리가 찾는 1번 컴퓨터와 인접한 컴퓨터가 없다면 빈 리스트라도 만들어주는 작업
        netdic[1] = []
    return netdic

print(com_find(change(netlist), 1))