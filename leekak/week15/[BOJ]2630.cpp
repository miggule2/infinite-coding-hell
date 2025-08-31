#include <iostream>
using namespace std;

int N;
int w_cnt=0, b_cnt=0;
int paper[128][128] = {0,};

// 크기가 n인 정사각형을 검사하는 재귀 함수
void cut(int y, int x, int n) {
    int color = paper[y][x];  // 기준 색
    bool flag = true;

    // n X n 영역이 모두 같은 색인지 검사
    for(int i=y; i<y+n; i++) {
        for(int j=x; j<x+n; j++) {
            if(paper[i][j] != color) {
                flag = false;
                break;
            }
        }
    }
    if(flag) {
        if(!color) w_cnt++;
        else b_cnt++;
    } else {
        cut(y, x, n/2);
        cut(y + n/2, x, n/2);
        cut(y, x + n/2, n/2);
        cut(y + n/2, x + n/2, n/2);
    }

}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    for(int i=0; i<N; i++)
        for(int j=0; j<N; j++)
            cin >> paper[i][j];

    cut(0, 0, N);
    cout << w_cnt << "\n" << b_cnt;
    return 0;
}
