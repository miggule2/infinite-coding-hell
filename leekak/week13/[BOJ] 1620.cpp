#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int N, M;
    cin >> N >> M;
    vector<string> pokemon_v(N+1);
    map<string, int> pokemon_m;
    for(int i=1; i<=N; i++) {
        string tmp;
        cin >> tmp;
        pokemon_v[i] = tmp;
        pokemon_m.insert({tmp, i});
    }
    for(int i=0; i<M; i++) {
        string tmp;
        cin >> tmp;
        if(tmp[0] >= '1' && tmp[0] <= '9') {
            int index = stoi(tmp);
            cout << pokemon_v[index] << "\n";
        } else {
            cout << pokemon_m[tmp] << "\n";
        }
    }
    return 0;
}
