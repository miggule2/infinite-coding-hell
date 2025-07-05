#include <bits/stdc++.h>

using namespace std;

int result[100001];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int len_sequence; cin >> len_sequence;
    result[0] = 0;
    for(int i = 1; i <= len_sequence; i++){
        int temp; cin >> temp;
        result[i] = max(temp, temp + result[i - 1]);
    }
    cout << *max_element(result + 1, result + len_sequence + 1);
}
