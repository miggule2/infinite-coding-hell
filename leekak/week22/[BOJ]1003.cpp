#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    vector<pair<int, int>> memo;  // 0 출력 횟수와 1 출력 횟수를 묶어 저장함
    for(int i=0; i<=40; i++) {
        if(i==0) memo.push_back(make_pair(1,0));
        else if(i==1) memo.push_back(make_pair(0,1));
        else {
            int a, b;
            a=memo[i-1].first+memo[i-2].first;    // 0
            b=memo[i-1].second+memo[i-2].second;  // 1
            memo.push_back(make_pair(a,b));
        }
    }
    for(int i=0; i<T; i++) {
        int tmp; cin >> tmp;
        cout << memo[tmp].first << " " << memo[tmp].second <<"\n";
    }
    return 0;
}
