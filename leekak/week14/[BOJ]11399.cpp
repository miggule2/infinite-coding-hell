#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    int result;
    cin >> N;
    vector<int> v(N);
    vector<int> sum(N);
    for(int i=0; i<N; i++) cin >> v[i];
    sort(v.begin(), v.end());
    sum[0] = v[0];
    result = sum[0];
    for(int i=1; i<N; i++) {
        sum[i] = sum[i-1] + v[i];
        result = result + sum[i];
    }
    cout << result;
    return 0;
}
