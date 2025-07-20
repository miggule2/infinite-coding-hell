#include <iostream>
#include <vector>
using namespace std;

vector<int> coin(10);
int cnt=0;

void recursive_coin(int K, int N) {
    if(K != 0) {
        int nearest=1;
        for(int i=0; i<N; i++) {
            if(coin[i] <= K) nearest = coin[i];
            else {
                nearest = coin[i-1];
                break;
            }
        }
        cnt = cnt + K / nearest;  //해당 동전을 몇 개 사용할 수 있는지 cnt에 저장
        K = K % nearest;
        recursive_coin(K, N);
    }
}

int main() {
    int N, K;
    cin >> N >> K;
    for(int i=0; i<N; i++) {
        int tmp;
        cin >> tmp;
        coin[i] = tmp;
    }
    recursive_coin(K, N);
    cout << cnt;
    return 0;
}
/*
동전의 종류를 vector에 저장
현재 금액 K보다 작거나 같은 동전 중에서 가장 큰 것을 사용한다
해당 동전을 몇 개 사용할 수 있는지 cnt에 저장
남은 금액에 대해 재귀적으로 반복하며 K가 0이 될 때까지 수행한다.
*/
