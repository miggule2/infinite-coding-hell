# 최소 높이 트리리
import collections

class Solution(object):
    def findMinHeightTrees(self, n, edges): # n: 노드 개수, edges: 간선 정보
        if n <= 1: 
            return [0]
        graph = collections.defaultdict(list)

        for i, j in edges: # 간선 정보로 그래프 생성
            graph[i].append(j) # 무방향 그래프이기 때문에 딕셔너리에 양방향으로 삽입
            graph[j].append(i)

        leaf_nodes = []  # leafnode들 추가
        for i in range(n + 1): # 노드 개수만큼 반복
            if len(graph[i]) == 1: # leafnode는 degree가 1인 노드
                leaf_nodes.append(i) # leafnode 추가
        while n > 2: # 노드 개수가 2개 이하가 될 때까지 반복
            n -= len(leaf_nodes) # leafnode 개수만큼 노드 개수 감소
            new_leafNodes = []
            for leaf in leaf_nodes: # leafnode들 반복
                popleaf = graph[leaf].pop() # leafnode의 부모 노드
                graph[popleaf].remove(leaf) # 부모 노드에서 leafnode 제거

                if len(graph[popleaf]) == 1: # 부모 노드의 degree가 1이면 leafnode로 추가
                    new_leafNodes.append(popleaf)  
            leaf_nodes = new_leafNodes # leafnode 리스트 갱신
        return leaf_nodes 