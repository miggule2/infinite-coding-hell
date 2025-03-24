#include <iostream>
#include <algorithm>
#include <limits.h>
using namespace std;

int main() {
    while(true) {
        int N;
        cin >> N;
        if(N==0) return 0; // 종료조건

        int income[N];
        int dp[N]; //dp[i], i를 오른쪽 끝으로 하는 구간의 최대 합으로 정의
        for(int i=0; i<N; i++) {
            cin >> income[i];
        }
        dp[0] = income[0];
        for(int i=1; i<N; i++) {
            dp[i] = max(income[i], dp[i-1]+income[i]);  // 새로 들어오는 값 또는 (직전까지의 합 + 새로 들어오는 값)이다.
        }
        int result = -INT_MAX;
        for(int i=0; i<N; i++) {
            if(dp[i] > result) result = dp[i];
        }
        cout << result << "\n";
    }
    return 0;
}
