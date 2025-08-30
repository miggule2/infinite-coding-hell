#include <iostream>
using namespace std;
int M, N, K;
bool visited[50][50];  // 방문 여부 확인
int map[50][50];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};

// 연결된 배추들을 하나의 무리로 보고 탐색
// connected component 찾기
void dfs(int x, int y) {
    visited[x][y] = true;  // 현재 위치 방문 처리
    int ax, ay;
    for(int i=0; i<4; i++) {
        ax = x + dx[i];
        ay = y + dy[i];

        if(ax<0 || ax>=M || ay<0 || ay>=N) continue;
        if(!visited[ax][ay] && map[ax][ay]==1) dfs(ax, ay);
    }
}

int main() {
    int T;
    cin >> T;
    while(T--) {
        int result=0;  // 필요한 지렁이의 수
        cin >> M >> N >> K;
      
        // 초기화
        for(int i=0; i<50; i++) {
            for(int j=0; j<50; j++) {
                map[i][j] = 0;
                visited[i][j] = false;
            }
        }
        while(K--) {
            int x, y;
            cin >> x >> y;
            map[x][y] = 1;
        }

        for(int i=0; i<M; i++) {
            for(int j=0; j<N; j++) {
                if(map[i][j] && !visited[i][j]) {
                    dfs(i, j);
                    result++;
                }
            }
        }
        cout << result << "\n";
    }
    return 0;
}
