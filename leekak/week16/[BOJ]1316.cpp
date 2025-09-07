#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;
    int result=0;
    for(int i=0; i<N; i++) {
        string str;
        cin >> str;
        vector<int> alphabet(26,0);
        for(int j=0; j<str.size(); j++) {
            if(j==0) {
                alphabet[str[j]-'a']++;
                if(str.size()-1 == 0) result++;
                continue;
            }
            if(str[j] != str[j-1]) {
                if(alphabet[str[j]-'a']==1) {
                    break;
                } else {
                    alphabet[str[j]-'a']++;
                }
            }
            if(j==str.size()-1) result++;
        }
    }
    cout << result;
    return 0;
}
