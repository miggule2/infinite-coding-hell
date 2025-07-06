#include <bits/stdc++.h>
using namespace std;

int result[500000];

int main(){
    ios::sync_with_stdio(0); cin.tie(0);
    int num_building;
    cin >> num_building;
    stack<pair<int, int>> building;

    for(int i = 0; i < num_building; i++){
        int temp;
        cin >> temp;

        if(!building.empty()){
            while(!building.empty() && building.top().first <= temp){
                building.pop();
            }
            if(!building.empty()) result[i] = building.top().second + 1;
        }
        building.emplace(temp, i);
    }

    for(int i = 0; i < num_building; i++) cout << result[i] << " ";
}