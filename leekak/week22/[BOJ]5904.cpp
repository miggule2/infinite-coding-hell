#include <iostream>
using namespace std;

void recursive(int N, int k, int len) {
    if(N<=3) {
        if(N==1) cout <<'m';
        else cout << 'o';
    } else {
        int new_len = len*2+k+3;
        if(N > new_len) recursive(N, k+1, new_len);
        else if(N>len && N<=len+k+3) {
            if(N-len != 1) cout << 'o';
            else cout << 'm';
            exit(0);
        } else recursive(N-(len+k+3),1, 3);
    }
}

int main() {
    int N;
    cin >> N;
    recursive(N, 1,3);
    return 0;
}
