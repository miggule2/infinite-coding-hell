#include <iostream>
#include <stack>

using namespace std;


bool check(string str) {
    stack<char> paren;  // 괄호 저장 스택
    for(int i=0; i<str.size(); i++) {
        if(str[i] == '(' || str[i] == '[') {
            // 여는 괄호 스택에 push
            paren.push(str[i]);
        }
        // 닫는 괄호일 때 검사
        if(str[i] == ')') {
            if(paren.empty() || paren.top() == '[') return false;
            else paren.pop();
        } else if(str[i] == ']') {
            if(paren.empty() || paren.top() == '(') return false;
            else paren.pop();
        }
    }
    // 스택이 비어있다면 통과!
    if(paren.empty()) return true;
    else return false;
}

int main() {
    while(true) {
        string tmp;
        getline(cin, tmp, '.');
        cin.ignore();
        if(tmp.empty()) break;
        if(check(tmp)) cout << "yes\n";
        else cout << "no\n";
    }

    return 0;
}
