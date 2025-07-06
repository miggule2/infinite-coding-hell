// 17298

#include <bits/stdc++.h>

using namespace std;

int num_of_nums;
stack<pair<int, int>> sequence;
pair<int, int> index_and_input;
vector<int> result;

int main(){
    cin >> num_of_nums;
    result.resize(num_of_nums, -1);
    int input;

    for(int i = 0; i < num_of_nums; i++){
        cin >> input;
        index_and_input = {i, input};

        while(!sequence.empty() && sequence.top().second < input){
            result[sequence.top().first] = input;
            sequence.pop();
        }

        sequence.push(index_and_input);
    }

    for(auto i : result) cout << i << " ";

    return 0;
}