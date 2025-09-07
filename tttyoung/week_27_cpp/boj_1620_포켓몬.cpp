#include <iostream>
#include <map>
#include <vector>
#include <unordered_map>
#include <cctype> //isdigit사용
#include <string> 

using namespace std;

int main()
{
    cin.tie(NULL); //시간초과 때문에 입출력 방식 바꿈
    ios_base::sync_with_stdio(false);
    int n, m;
    cin >> n >> m;
    vector<string> num_to_name(n + 1); //번호로 이름 출력
    unordered_map<string, int> name_to_num; //이름으로 번호출력

    for (int i = 1; i <= n; i++) {
        string name;
        cin >> name;
        num_to_name[i] = name;
        name_to_num[name] = i;
    }
    while (m--) {
        string x;
        cin >> x;
        if (isdigit(x[0])) { //만약 숫자라면
            int result = stoi(x); //string으로 받았으므로 int형으로 바꿔줌
            cout << num_to_name[result]<<"\n";
        }
        else {
            cout << name_to_num[x]<<"\n";
        }
    }
}

