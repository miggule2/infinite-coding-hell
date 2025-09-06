#include <iostream>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

int main(){
    double sum = 0;
    double result = 0;

    map<string,double> map;

    map["A+"] = 4.5;
    map["A0"] = 4.0;
    map["B+"] = 3.5;
    map["B0"] = 3.0;
    map["C+"] = 2.5;
    map["C0"] = 2.0;
    map["D+"] = 1.5;
    map["D0"] = 1.0;
    map["F"] = 0.0;


    for(int i = 0; i < 20; i++){
        string s;
        double f;
        string grade;

        cin >> s >> f >> grade;

        if(grade=="P") continue;
        sum += f;
        result += f*map[grade];

    }

    cout << setprecision(6)<<result/sum << endl;
}