#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main(){
    int n = 0;
    cin >> n;

    map<int, vector<string>, greater<int>> map;
    for(int i = 0; i < n; i++){
        string s;
        int k;
        cin >> s >> k;
        map[k].push_back(s);
    }

    bool isNone = true;
    string result = "NONE";
    for(auto it = map.begin(); it != map.end(); it++){
        if(it->second.size() == 1) {
            result = it->second[0];
            isNone = false;
            break;
        } 
    }

    cout << result << endl;
    return 0;
}