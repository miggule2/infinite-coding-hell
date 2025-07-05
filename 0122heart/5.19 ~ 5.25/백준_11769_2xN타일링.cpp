#include <bits/stdc++.h>

using namespace std;

int result[1000];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int target; cin >> target;
    result[0] = 1;
    result[1] = 2;
    for(int i = 2; i < target; i++) result[i] = (result[i - 1] + result[i - 2]) % 10007;
    cout << result[target - 1];
    return 0;
}
