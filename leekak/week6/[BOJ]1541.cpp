#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string str;
    vector<string> str_split;
    vector<int> term;
    cin >> str;

    int cnt_plus=0;
    size_t pos;
    while((pos = str.find('-')) != string::npos)  {
        str_split.push_back(str.substr(0, pos)); // 찾은 데까지 저장
        str.erase(0, pos + 1); // 찾은 만큼은 지워 주자
    }//npos는 find()가 검색에 실패했을 때 반환하는 값임
    str_split.push_back(str.substr(0, pos)); // 마지막에 남은 식

    for(int i=0; i<str_split.size(); i++) {
        while((pos = str_split[i].find('+')) != string::npos)  {
            //i==0일 때 이 부분이 수행된다는 것은 '+'가 먼저 나온다는 것
            if(i==0) {
                cnt_plus++;
            }
            term.push_back(stoi(str_split[i].substr(0, pos)));
            str_split[i].erase(0, pos + 1);
        }
        term.push_back(stoi(str_split[i].substr(0, pos)));

    }

    int result = term[0];

    // cnt==0 이면 '-'가 먼저 나온다는 것임
    for(int i=1; i<cnt_plus+1; i++) {
        result += term[i];
    }
    for(int i=cnt_plus+1; i<term.size(); i++) {
        result -= term[i];
    }

    cout << result;

    return 0;
}
