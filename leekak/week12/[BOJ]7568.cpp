#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int main() {
    int N;
    cin >> N;
    vector<tuple<int, int, int>> v;
    for(int i=0; i<N; i++) {
        int first, second;
        cin >> first >> second;
        v.push_back(make_tuple(first, second, 1));
    }
    for(int i=0; i<N-1; i++) {
        for(int j=i+1; j<N; j++) {
            if(get<0>(v[i]) > get<0>(v[j])) {
                if(get<1>(v[i]) > get<1>(v[j])) {
                    get<2>(v[j])++;
                }
            } else if(get<0>(v[i]) < get<0>(v[j])) {
                if(get<1>(v[i]) < get<1>(v[j])) {
                    get<2>(v[i])++;
                }
            }
        }
    }
    for(int i=0; i<N; i++) {
        cout << get<2>(v[i]) << " ";
    }
    return 0;
}
