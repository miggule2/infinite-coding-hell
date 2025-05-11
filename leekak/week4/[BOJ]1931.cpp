#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<pair<int, int>> meeting;
    for(int i=0; i<N; i++) {
        int tmp1, tmp2;
        cin >> tmp1 >> tmp2;
        meeting.emplace_back(tmp2, tmp1); // 끝나는 시간을 first로 저장
    }
    sort(meeting.begin(), meeting.end());
    int result=0, earliest=0; // earliest: 현재 가장 빨리 끝나는 시간
    for(int i=0; i<N; i++) {
        int begin = meeting[i].second;
        int end = meeting[i].first;
        if(earliest <= begin) { // 시간이 겹치지 않을 경우
            earliest = end;
            result++;
        }
    }
    cout << result;
    return 0;
}
