#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<int> sum_arr(N+1, 0);
    for(int i=1; i<=N; i++)  {
        int tmp;
        cin >> tmp;
        sum_arr[i] = sum_arr[i-1] + tmp;
    }
    for(int i=0; i<M; i++) {
        int start, end;
        cin >> start >> end;
        cout << sum_arr[end]-sum_arr[start-1] << "\n";
    }
    return 0;
}
