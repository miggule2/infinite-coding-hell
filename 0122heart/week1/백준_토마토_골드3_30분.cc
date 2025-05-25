// 2579

#include <bits/stdc++.h>
using namespace std;

struct coordi{
    int r, c, h;
    coordi(int h, int r, int c) : r(r), c(c), h(h){}
};

int d_row[] = {1, 0, 0, -1, 0, 0}, d_col[] = {0, 1, 0, 0, -1, 0}, d_height[] = {0, 0, 1, 0, 0, -1};
int num_row, num_col, num_height;
int board[101][101][101];
queue<coordi> frontier;

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    cin >> num_col >> num_row >> num_height;
    bool complete = true;
    for(int i = 0; i < num_height; i++){
        for(int j = 0; j < num_row; j++){
            for(int k = 0; k < num_col; k++){
                cin >> board[i][j][k];
                if(board[i][j][k] == 1) frontier.emplace(i, j, k);
                if(!board[i][j][k]) complete = false;
            }
        }
    }

    // 안 익은 토마토가 없을 때
    if(complete){
        cout << 0;
        return 0;
    }

    int result = 0;
    while(!frontier.empty()){
        coordi now = frontier.front(); frontier.pop();
        for(int dir = 0; dir < 6; dir++){
            int n_row = now.r + d_row[dir];
            int n_col = now.c + d_col[dir];
            int n_height = now.h + d_height[dir];
            if(n_row < 0 || num_row <= n_row ||
                n_col < 0 || num_col <= n_col ||
                n_height < 0 || num_height <= n_height) continue;
            if(board[n_height][n_row][n_col]) continue;
            board[n_height][n_row][n_col] = board[now.h][now.r][now.c] + 1;
            if(result < board[n_height][n_row][n_col]) result = board[n_height][n_row][n_col];
            frontier.emplace(n_height, n_row, n_col);
        }
    }

    for(int i = 0; i < num_height; i++){
        for(int j = 0; j < num_row; j++){
            if(any_of(board[i][j], board[i][j] + num_col, [](int x){return x == 0;})){
                cout << -1;
                return 0;
            }
        }
    }

    cout << result - 1;
}
