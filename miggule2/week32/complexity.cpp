#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(){
    stack<char> charStack;
    string line;
    while(getline(cin, line)){
        for(char ch : line){
            if(ch == '{' || ch == '}') charStack.push(ch);
        }
    }

    int level = 0;
    int result = 0;
    while(!charStack.empty()){
        if(charStack.top() == '}') {level++; charStack.pop();}
        else{
            charStack.pop();
            result += level;
            level--;
        }
    }

    cout << result;
}