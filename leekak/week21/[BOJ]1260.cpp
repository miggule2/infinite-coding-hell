#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int N, M, V;
vector<vector<int>> graph;
vector<bool> visited;
vector<bool> discovered;

void dfs(int here) {
    cout << here << " ";
    visited[here] = true;
    for(int i=0; i<graph[here].size(); i++) {
        int visit = graph[here][i];
        if(!visited[visit]) dfs(visit);
    }
}

vector<int> bfs(int start) {
    queue<int> q;
    vector<int> order;
    discovered[start] = true;
    q.push(start);

    while(!q.empty()) {
        int here = q.front();
        q.pop();
        order.push_back(here);
        for(int i=0; i<graph[here].size(); i++) {
            int visit = graph[here][i];
            if(!discovered[visit]) {
                q.push(visit);
                discovered[visit] = true;
            }
        }
    }
    return order;
}

int main() {
    cin >> N >> M >> V;
    for(int i=0; i<N+1; i++) {
        vector<int> v;
        graph.push_back(v);
    }

    for(int i=0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    for(int i=1; i<N+1; i++) {
        sort(graph[i].begin(), graph[i].end());
    }

    visited = vector<bool> (graph.size(), false);
    dfs(V);
    cout << "\n";

    discovered = vector<bool> (graph.size(), false);
    vector<int> BFS = bfs(V);
    for(int i=0; i<BFS.size(); i++) {
        cout << BFS[i] << " ";
    }
    return 0;
}
