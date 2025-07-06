#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N, L;
    cin >> N >> L;
    vector<int> cracked(N);
    for(int i=0; i<N; i++) {
        cin >> cracked[i];
    }
    sort(cracked.begin(), cracked.end());
    int start = cracked[0];
    int diff = 0;
    int result = 1;
    for(int i=1; i<N; i++) {
        diff = cracked[i] - start;
        if((diff+1) > L) {
            result++;
            start = cracked[i];
        }
    }
    cout << result;
    return 0;
}
