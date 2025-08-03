#include <iostream>
#include <set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    multiset<int> DS;
    while(N--) {
        int tmp;
        cin >> tmp;
        if(tmp == 0) {
            if(DS.empty()) cout << 0 << "\n";
            else {
                cout << *DS.begin() << "\n";
                DS.erase(DS.begin());
            }
        } else {
            DS.insert(tmp);
        }
    }
    return 0;
}
