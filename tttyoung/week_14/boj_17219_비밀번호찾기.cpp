#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    std::unordered_map<std::string, std::string> userDatabase; //c++에서 딕셔너리 사용하는 방법
    
    int n, m;
    cin >> n >> m;
    // 사용자 추가
    for (int i = 0; i < n; i++) {
        string id, pw;
        cin >> id >> pw;
        userDatabase[id] = pw;
    }

    for (int i = 0; i < m; i++) {
        string finding_id;
        cin >> finding_id;
        cout << userDatabase[finding_id] << "\n";
    }

    return 0;
}