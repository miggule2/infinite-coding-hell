#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> prices) {
    stack<pair<int, int>> record;

    // 가격 순회하면서 스택에 넣고 빼기
    for(int i = 0; i < prices.size(); i++){
        // 빼기
        while(!record.empty() && prices[i] < record.top().first){
            auto now = record.top(); record.pop();
            prices[now.second] = i - now.second;
        }

        // 넣기
        record.emplace(prices[i], i);
    }

    while(!record.empty()){
        auto now = record.top(); record.pop();
        prices[now.second] = prices.size() - 1 - now.second;
    }

    return prices;
}