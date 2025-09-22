#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> sorting(char cmd, int num, int k, vector<vector<int>>& waitingroom) {
    if (cmd == '+') { //"+" 가 입력되었을때
        if (waitingroom.empty()) { //처음으로 입력해주는경우(대기실이 비어있을때)
            waitingroom.push_back({ num });
            return waitingroom;
        }

        int idx = -1; //초기 index값
        if (num < waitingroom[0].front()) { //맨 처음 의자 맨 앞에 위치해야할 경우
            idx = 0;
        }
        else if (num> waitingroom.back().back()){ //맨 마지막 의자 맨 뒤에 위치해야할 경우
            idx = (int)waitingroom.size() - 1;
        }
        else { 
            for (int i = 0; i < size(waitingroom); i++) {
                if (waitingroom[i].front() <= num && waitingroom[i].back() >= num) { //의자 중간에 들어가는 경우
                    idx = i;
                    break;
                } 
                //의자와 의자 사이의 중간값을 가지는 경우
                else if (waitingroom[i].back() <= num && waitingroom[i + 1].front() > num) { 
                    idx = i;
                }
            }
        }

        waitingroom[idx].push_back(num);
        sort(waitingroom[idx].begin(), waitingroom[idx].end()); //추가하고 sort해줘야 적절한 index를 가짐
        if (waitingroom[idx].size() == 2*k) { //의자 나누기
            vector<int> left(waitingroom[idx].begin(), waitingroom[idx].begin() + k);
            vector<int> right(waitingroom[idx].begin() + k, waitingroom[idx].end());
            waitingroom.erase(waitingroom.begin() + idx);
            waitingroom.insert(waitingroom.begin() + idx, left);
            waitingroom.insert(waitingroom.begin() + idx + 1, right);
        }
    }

    else { // "-" 입력을 받았을 경우
        for (int i = 0; i < waitingroom.size(); i++) {
            //값이 중간에 있는 경우
            if (find(waitingroom[i].begin(), waitingroom[i].end(), num) != waitingroom[i].end()) {
                //waitingroom[i].erase(remove(waitingroom[i].begin(), waitingroom[i].end(), num), waitingroom[i].end());
                waitingroom[i].erase(find(waitingroom[i].begin(), waitingroom[i].end(), num)); //해당 대기번호 삭제
                if (waitingroom[i].empty()) { //삭제 후 의자가 비어있을 경우 -> 의자 삭제
                    waitingroom.erase(waitingroom.begin() + i);
                }
                break;
            }
        }

    }
    return waitingroom;
}
    
int main()
{
    vector <vector<int>> waitingroom;
    int n, k;
    cin >> n >> k;
    
    for (int i = 0; i < n; i++) {
        char cmd;
        int num;
        cin >> cmd >> num;
        waitingroom = sorting(cmd, num, k, waitingroom);
    }

    for (auto& result : waitingroom) {
        cout << result.front() << "\n";
    }
}

/*
void sorting(char cmd, int num, vector<vector<int>>& waitingroom, vector<int> &tail) {
    if (cmd == '+') {
        if (waitingroom.empty()) {
            waitingroom.push_back({ num });
        }
        int i = lower_bound(tail.begin(), tail.end(), num) - tail.begin();
        if (i == tail.size()) {
            waitingroom.push_back({ num });
        }
        else waitingroom[i].push_back(num);
    }
    else {
            return;
    }
}
*/