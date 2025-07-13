#include <iostream>
#include <set>
#include <cstdlib>
using namespace std;

int main() {
    multiset<pair<int, int>> abs_heap;
    multiset<pair<int, int>>::iterator iter;
    int N;  cin >> N;
    while(N--) {
        int x;  cin >> x;
        if(x==0) {
            if(abs_heap.empty())
                cout << 0 <<"\n";
            else {
                iter = abs_heap.begin();
                cout << iter->second << "\n";
                abs_heap.erase(iter);
            }
        } else {
            int abs_x = abs(x);
                abs_heap.insert(make_pair(abs_x, x));
        }
    }
    return 0;
}
