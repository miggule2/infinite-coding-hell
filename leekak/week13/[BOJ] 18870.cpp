#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> coord;
    for(int i=0; i<N; i++) {
        int tmp;
        cin >> tmp;
        coord.push_back(tmp);  // 원본 좌표 저장
    }
    // 복사본
    vector<int> order(coord);
    sort(order.begin(), order.end());
    // 중복 값 제거
    order.erase(unique(order.begin(), order.end()), order.end());
    for(int i=0; i<N; i++) {
        // coord[i] 값이 들어갈 수 있는 첫 인덱스를 반환
        auto it = lower_bound(order.begin(), order.end(), coord[i]);
        cout << it - order.begin() << " ";
    }
    return 0;
}
