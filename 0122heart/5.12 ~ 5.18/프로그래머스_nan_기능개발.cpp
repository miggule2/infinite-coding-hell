#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    int index = 0;
    vector<int> answer;
    while(index < progresses.size()){
        int time = (100 - progresses[index]) / speeds[index];
        if((100 - progresses[index]) % speeds[index] != 0) time++;

        int temp_result = 1;
        int i = index + 1;
        while(i < progresses.size() && progresses[i] + speeds[i] * time >= 100){
            temp_result++;
            i++;
        }
        answer.push_back(temp_result);
        index = i;
    }
    return answer;
}
