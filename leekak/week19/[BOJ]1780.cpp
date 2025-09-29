#include <iostream>
using namespace std;

int cnt_n=0;
int cnt_zero=0;
int cnt_p=0;
int paper[2200][2200];

// (x,y)를 좌상단으로 하고 크기 N인 정사각형이
// 한 가지 값(-1, 0, 1)으로만 이루어져 있으면 해당 값을 카운트,
// 아니면 3x3으로 나눠 9개 영역을 재귀 호출
void cut_paper(int x, int y, int N){
    bool flag=1;
    for(int i=y; i<y+N; i++) {
        for(int j=x; j<x+N; j++) {
            if(paper[y][x] != paper[i][j]) {
                flag=0; //0이면 다름
                break;
            }
        }
        if(flag==0) break;
    }
    if(flag==0) {
        cut_paper(x, y, N/3);
        cut_paper(x, y+N/3, N/3);
        cut_paper(x, y+N/3+N/3, N/3);
        cut_paper(x+N/3, y, N/3);
        cut_paper(x+N/3, y+N/3, N/3);
        cut_paper(x+N/3, y+N/3+N/3, N/3);
        cut_paper(x+N/3+N/3, y, N/3);
        cut_paper(x+N/3+N/3, y+N/3, N/3);
        cut_paper(x+N/3+N/3, y+N/3+N/3, N/3);

    } else {
        if(paper[y][x]==-1) cnt_n++;
        else if(paper[y][x]==0) cnt_zero++;
        else if(paper[y][x]==1) cnt_p++;
    }
}

int main() {
    int N;
    cin >> N;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cin >> paper[i][j];
        }
    }
    cut_paper(0,0, N);
    cout << cnt_n << "\n" << cnt_zero << "\n" << cnt_p;
    return 0;
}
