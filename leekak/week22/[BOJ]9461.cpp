#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    unsigned long long dp[101] = {0, };
    dp[0] = 1;
    dp[1] = 1;
    dp[2] = 1;
    dp[3] = 2;
    dp[4] = 2;
    for(int i=5; i<100; i++) {
        dp[i] = dp[i-1] + dp[i-5];
    }
    while(T--) {
        int N;
        cin >> N;
        cout << dp[N-1] << "\n";
    }

    return 0;
}
