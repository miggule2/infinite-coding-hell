#include <iostream>
using namespace std;
int w, h;
bool visited[50][50];
int map[50][50];
int dx[8] = {-1, 0, 1, 0, -1, -1, 1, 1};
int dy[8] = {0, -1, 0, 1, -1, 1, -1, 1};
// 대각선도 고려해야 함

void dfs(int x, int y) {
    visited[x][y] = true;  // 현재 위치 방문 표시
    int ax, ay;
    for(int i=0; i<8; i++) {
        ax = x + dx[i];
        ay = y + dy[i];

        if(ax<0 || ax>=h || ay<0 || ay>=w) continue;
        // 아직 방문하지 않았고, 땅인 경우에만 dfs 수행
        if(!visited[ax][ay] && map[ax][ay]==1) dfs(ax, ay);
    }
}

int main() {
    while(!cin.eof()) {
        int result=0;
        cin >> w >> h;
        if(w==0 && h==0) break;
        // map과 방문 배열 초기화
        for(int i=0; i<50; i++) {
            for(int j=0; j<50; j++) {
                map[i][j] = 0;
                visited[i][j] = false;
            }
        }
        for(int i=0; i<h; i++) {
            for(int j=0; j<w; j++) {
                cin >> map[i][j];
            }
        }
        for(int i=0; i<h; i++) {
            for(int j=0; j<w; j++) {
                // 방문하지 않았고 땅인 경우, 결과 추가
                if(map[i][j] && !visited[i][j]) {
                    result++;
                    dfs(i, j);
                }
            }
        }
        cout << result << "\n";
    }

    return 0;
}
/*
* 모든 위치에 대해 dfs 수행
* 방문한 적이 없고, 땅인 경우에만 dfs를 수행하고 섬의 개수 추가
*/
