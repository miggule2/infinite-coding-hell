#include <iostream>
#include <map>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int i=0; i<T; i++) {
        int n;
        cin >> n;
        int result=1;
        map<string, int> closet;
        for(int j=0; j<n; j++) {
            string tmp;
            string part;
            cin >> tmp >> part;

            if(closet.find(part) == closet.end()) {
                closet.insert({part, 1});
            } else {
                closet[part] = closet[part] + 1;
            }

        }
        for(auto iter = closet.begin(); iter != closet.end(); iter++) {
                result = result * (iter->second+1);
        }
        cout << result - 1 << "\n";
    }
    return 0;
}
