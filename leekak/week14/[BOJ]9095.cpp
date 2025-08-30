#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v(11);
    v[0] = 1;
    v[1] = 2;
    v[2] = 4;
    for(int i=3; i<11; i++) {
        v[i] = v[i-1] + v[i-2] + v[i-3];
    }
    int T;
    cin >> T;
    for(int i=0; i<T; i++) {
        int tmp;
        cin >> tmp;
        cout << v[tmp-1] << "\n";
    }
    return 0;
}
