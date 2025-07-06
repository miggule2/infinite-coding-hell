#include <iostream>
using namespace std;

int main() {
    int N, M;
    cin >> N >> M;
    int min_pack = 1000;
    int min_one = 1000;
    int t1, t2;
    for(int i=0; i<M; i++) {
        cin >> t1 >> t2;
        if(t1 < min_pack) min_pack = t1;
        if(t2 < min_one) min_one = t2;
    }
    if(min_one*6 < min_pack) {  // 묶음으로 사는 것 보다 낱개로 사는 것이 더 저렴한 경우
        cout << N*min_one;
    } else {
        if((N%6)==0) cout << (N/6)*min_pack;
        else {
            if((N%6)*min_one < min_pack ) {
                cout << (N/6)*min_pack + (N%6)*min_one;
            } else {
                cout << ((N/6)+1)*min_pack;
            }
        }
    }

    return 0;
}
