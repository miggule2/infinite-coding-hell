#include <iostream>
using namespace std;

int R, C, K;
char map[5][5];
bool visited[5][5];
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, -1, 0, 1};
int result=0;

void dfs(int y, int x, int dist) {
    visited[y][x] = true;

    if(dist==K && y==0 && x==C-1) {
        // 성공
        result++;
        return;
    }

    for(int i=0; i<4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(ny<0 || ny>=R || nx<0 || nx>=C) continue;
        if(map[ny][nx] == 'T') continue;

        if(map[ny][nx] == '.' && !visited[ny][nx] && dist<K) {
            dfs(ny, nx, dist+1);
            visited[ny][nx]= false;
        }
    }
}

int main() {
    cin >> R >> C >> K;
    for(int i=0; i<R; i++) {
        for(int j=0; j<C; j++) {
            cin >> map[i][j];
        }
    }
    dfs(R-1, 0, 1);
    cout << result;

    return 0;
}
/*
 * 거리를 늘려가며 이동
 * 거리가 K를 넘으면 즉시 종료
 * 도착위치이고 거리와 K가 같을 때 카운트
 *
 * 이미 visited가 true로 바꼈기 때문에 한 번 제대로된 경로를 탐색하면 더 안됨
 * -> 어카지
 * -> 고냥 호출 뒤에 다시 false로 바꿔주면 되걸랑요
 */
