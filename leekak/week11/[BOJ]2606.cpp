#include <iostream>
#include <vector>
using namespace std;

// 인접 리스트
vector<vector<int>> graph;
vector<bool> visited;
// 감염된 컴퓨터 수
int cnt=0;

void dfs(int here) {
    cnt++;
    visited[here] = true;
    // 연결된 모든 인접 노드 탐색
    for(int i=0; i<graph[here].size(); i++) {
        int visit = graph[here][i];
        if(!visited[visit]) dfs(visit);  // 방문 안 했다면 -> 재귀적으로 방문
    }
}

int main() {
    int n_com, n_net;
    cin >> n_com >> n_net;
    for(int i=0; i<n_com+1; i++) {
        vector<int> v;
        graph.push_back(v);
    }
    for(int i=0; i<n_net; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }
    // 방문 배열 초기화
    visited = vector<bool> (graph.size(), false);
    dfs(1);
    // 자기 자신을 제외한 감염 컴퓨터 수 출력
    cout << cnt-1;
    return 0;
}
