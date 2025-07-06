// 6198

#include <bits/stdc++.h>

using namespace std;

int num_towers;
uint64_t result = 0;
stack<uint64_t> towers;

void setting(){
    cin >> num_towers;
}

void process(){
    uint64_t height;

    for(int tower = 0; tower < num_towers; tower++){
        cin >> height;

        while(!towers.empty() && towers.top() <= height){
            towers.pop();
        }

        towers.push(height);
        result += towers.size() - 1;
    }
}

int main(){
    setting();
    process();
    cout << result;
    return 0;
}