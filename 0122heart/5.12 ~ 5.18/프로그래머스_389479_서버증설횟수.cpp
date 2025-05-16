#include <bits/stdc++.h>

using namespace std;

vector<pair<int, int>> servers;
int result = 0;
int num_servers = 0;

int solution(vector<int> players, int m, int k) {
    for(int i = 0; i < players.size(); i++){
        if(!servers.empty()){
            for(auto &server : servers){
                server.second--;
            }
            if(servers[0].second == 0){
                num_servers -= servers[0].first;
                servers.erase(servers.begin());
            }
        }

        int now = players[i];
        if(m * num_servers + m <= now){
            int add = (now - m * num_servers) / m;
            result += add;
            num_servers += add;
            servers.emplace_back(add, k);
        }
    }

    return result;
}