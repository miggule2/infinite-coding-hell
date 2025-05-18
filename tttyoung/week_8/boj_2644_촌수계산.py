from collections import defaultdict 

num = int(input())
a, b = map(int, input().split())
edgenum = int(input())
edgelist = []
for i in range(edgenum):
    edgelist.append(list(map(int, input().split())))

edgedic= {}
for i in range(num):
    edgedic[i+1] = []
for x, y in edgelist:
    if x in edgedic:
        edgedic[x].append(y)
    if y in edgedic:
        edgedic[y].append(x)


def bfs(edgelist, start, end):
    qu = []
    done = set()
    count = 0

    qu.append(start)
    done.add(start)
    flag = False
    while qu:
        count+=1 #count를 pop하기 전의 qu의 갯수 동안은 동일하게 유지해야함.
        
        for i in range(len(qu)):
            p = qu.pop(0)
            if p == end:
                flag = True #만약 end값을 만나게 된다면 나머지 while문을 돌지 않고 그대로 나가게 하기
                #end값을 만나더라도 while문이 반복되게 된다면 나머지 노드들을 방문하면서 count값이 커지게됨. 그러면 우리가 원하는 end지점까지의 촌수가 아닌 다른 count값이 나오게됨.
                break

            for i in edgelist[p]:
                if i not in done:
                    qu.append(i)
                    done.add(i)        
        if flag == True:
            break
            
    if end in done:
        print(count-1)                                
    else:
        print(-1)
    
bfs(edgedic, a, b)


#count를 언제 해야할지, end를 찾았을대 어떻게 종료할지, 찾지못했을때 -1 출력
