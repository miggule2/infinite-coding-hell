#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const pair<int, int>&a, const pair<int, int>&b) {
    if(a.first == b.first) {
        return a.second < b.second;
    }
    return a.first < b.first;
}

int main() {
    int N;
    cin >> N;
    vector<pair<int, int>> v;
    for(int i=0; i<N; i++) {
        int first, second;
        cin >> first >> second;
        v.push_back(make_pair(first, second));
    }
    sort(v.begin(), v.end(), cmp);
    for(int i=0; i<N; i++) {
        cout << v[i].first << " " << v[i].second << "\n";
    }
    return 0;
}
