#include <bits/stdc++.h>
using namespace std;

stack<int> result;
stack<pair<int, int>> persistent;

void persist(int num_persistent){
    while(num_persistent--){
        auto now = persistent.top(); persistent.pop();
        if(now.first == 1) result.push(now.second);
        else result.pop();
    }
}

void process(){
    int cmd; cin >> cmd;
    switch(cmd){
    case 1:
        int input; cin >> input;
        result.push(input);
        persistent.emplace(2, 0);
        break;
    case 2:
        persistent.emplace(1, result.top());
        result.pop();
        break;
    case 3:
        int num_persistent; cin >> num_persistent;
        persist(num_persistent);
        break;
    case 4:
        cout << result.size() << "\n";
        break;
    case 5:
        if(!result.empty()) cout << result.top() << "\n";
        else cout << -1 << "\n";
        break;
    }
}

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int num_cmd; cin >> num_cmd;
    while(num_cmd--){
        process();
    }
    return 0;
}