#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    int n;
    int index=1;
    vector<char> result;
    cin >> n;
    vector<int> v;
    stack<int> s;
    for(int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        v.push_back(tmp);
    }
    auto it = v.begin();
    s.push(index);
    result.push_back('+');
    index++;
    while(it!=v.end()) {
        if(s.empty()) {
            s.push(index);
            result.push_back('+');
            index++;
        }
        if(s.top() > n) {
            cout << "NO";
            return 0;
        }
        if(s.top() == *it) {
            s.pop();
            result.push_back('-');
            it++;
            continue;
        }
        s.push(index);
        result.push_back('+');
        index++;
    }
    for(int i=0; i<result.size(); i++) {
        cout<< result[i] << "\n";
    }
    return 0;
}
