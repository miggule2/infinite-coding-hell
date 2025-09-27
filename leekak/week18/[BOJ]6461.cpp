#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    unsigned long long dp[101] = {0, };
    // 초기화
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    dp[4] = 2;
    // 점화식 p(n) = p(n-1) + p(n-5) (n>=6)
    for(int i=5; i<100; i++) {
        dp[i] = dp[i-1] + dp[i-5];
    }
    while(T--) {
        int N;
        cin >> N;
        cout << dp[N-1] << "\n";  //dp 배열은 0-index 이므로 dp[n-1]에 저장
    }

    return 0;
}
