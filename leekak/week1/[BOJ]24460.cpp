#include <iostream>
#include <string.h>
#include <algorithm>
using namespace std;

int arr[1024][1024] = {0, };

int devide(int x, int y, int n) {
    int result[4] = {0,};
    if(n >=2) {
        n /= 2;
        result[0] = devide(x, y, n);
        result[1] = devide(x, y+n, n);
        result[2] = devide(x+n, y, n);
        result[3] = devide(x+n, y+n, n);
        sort(result, result+4);
        return result[1];   //2번째 작은 번호 선택
    } else return arr[x][y];
}

int main() {
    int N;
    cin >> N;
    memset(arr, 0, sizeof(int) * N*N);
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cin >> arr[i][j];
        }
    }
    if(N==1) cout << arr[0][0];
    else cout << devide(0, 0, N);

    return 0;
}
