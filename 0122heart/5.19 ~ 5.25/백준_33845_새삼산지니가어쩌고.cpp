#include <bits/stdc++.h>

using namespace std;

bool result[1000];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    string except_string; cin >> except_string;
    set<char> except_set(except_string.begin(), except_string.end());
    string original_string; cin >> original_string;
    for(auto i : original_string){
        if(except_set.find(i) == except_set.end()) cout << i;
    }
    return 0;
}