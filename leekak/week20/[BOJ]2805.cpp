#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int N;
    long long M;
    long long start=0, end, result;
    cin >> N >> M;
    vector<long long> tree;
    for(int i=0; i<N; i++) {
        long long tmp;
        cin >> tmp;
        tree.push_back(tmp);  // 각 나무의 높이 입력
    }
    // 절단기 높이의 max는 가장 큰 나무의 높이
    end = *max_element(tree.begin(), tree.end());
    // binary search
    while(start <= end) {
        long long tmp = (start + end) / 2;  // 절단기 높이 후보
        long long take=0;
        // 각 나무를 절단기 높이(mid) 기준으로 잘랐을 때 얻을 수 있는 나무 길이 계산
        for(int i=0; i<N; i++) {
            if(tree[i] >= tmp) take = take + tree[i]-tmp;
        }
      // 필요한 양보다 많이 잘랐으면 길이 조정
        if(take >= M) {
            result = tmp;
            start = tmp + 1;
        } else {
            end = tmp - 1;
        }

    }
    cout << result;
    return 0;
}
