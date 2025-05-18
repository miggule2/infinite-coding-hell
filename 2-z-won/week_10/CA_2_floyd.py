INF = int(1e9)

def getInput():
    n = int(input())
    graph_info = []
    for _ in range(n):
        weight = list(map(int, input().split()))
        graph_info.append(weight)
    From, To = map(int, input().split())
    return n, graph_info, From, To

def floyd(graph_info):
    n = len(graph_info)
    weight = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(INF)
        weight.append(row)
    
    Next = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(None)
        Next.append(row)
    
    for i in range(n):
        for j in range(n):
            if graph_info[i][j] != -1:
                weight[i][j] = graph_info[i][j]
                Next[i][j] = j
        weight[i][i] = 0
        Next[i][i] = i
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if weight[i][k] + weight[k][j] < weight[i][j]:
                    weight[i][j] = weight[i][k] + weight[k][j]
                    Next[i][j] = Next[i][k]
    return weight, Next

def new_path(From, To, Next):
    if Next[From][To] is None:
        return []
    path = [From]
    while From != To:
        From = Next[From][To]
        path.append(From)
    return path

def displayOutput(From, To, cost, path):
    print("Shortest cost from {} to {}: {}".format(From, To, cost))
    print("Path from {} to {}: {}".format(From, To, path))

def main():
    n, graph_info, From, To = getInput()
    weight, Next = floyd(graph_info)

    cost = weight[From][To]
    if cost >= INF:
        path = []
    else: 
        path = new_path(From, To, Next)
    if cost < INF:
        cost = cost
    else: cost = INF
    displayOutput(From, To, cost, path)

if __name__ == "__main__":
    main()