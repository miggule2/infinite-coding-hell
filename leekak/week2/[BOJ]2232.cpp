#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> P(N);
    for(int i=0; i<N; i++) {
        cin >> P[i];
    }
    vector<int> result;

    if(N==1) {
        result.push_back(0);
    } else {
        if(P[0]>=P[1]) result.push_back(0);
        for(int i=1; i<N-1; i++) {
            if((P[i] >= P[i-1]) && (P[i] >= P[i+1])) {
                result.push_back(i);
            }
        }
        if(P[N-1]>=P[N-2]) result.push_back(N-1);
    }

    sort(result.begin(), result.end());
    for(int i=0; i<result.size(); i++) {
        cout << result[i]+1 << "\n";
    }

    return 0;
}
