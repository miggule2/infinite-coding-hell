#include <bits/stdc++.h>

using namespace std;

// 문제를 풀 때 자료형의 범위를 잘 체크해야함. 근데 이걸 어떻게 알 수 있지??
long long result[90][2];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int target; cin >> target;
    result[0][0] = 0;
    result[0][1] = 1;
    for(int i = 1; i < target; i++){
        result[i][0] = result[i - 1][0] + result[i - 1][1];
        result[i][1] = result[i - 1][0];
    }
    cout << result[target - 1][0] + result[target - 1][1];
}
