#include <iostream>
#include <set>

using namespace std;

int main(){
    int n;
    cin >> n;

    cin.ignore();

    set<char> set;
    int count = 0;
    char prev_char = '\0';

    for(int i = 0; i < n; i++){
        string str;
        getline(cin,str);
        bool isGroupWord = true;
        for(int j = 0; j < str.length();j++){
            if(set.count(str[j])>=1 && prev_char != str[j]) {
                isGroupWord = false;
                break;
            } else{
                set.insert(str[j]);
            }
            prev_char = str[j];
        }
        
        if(isGroupWord) count++;
        set.clear();
    }

    cout << count;
}