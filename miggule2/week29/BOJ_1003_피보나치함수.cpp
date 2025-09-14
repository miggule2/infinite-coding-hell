#include <iostream>
#include <unordered_map>

using namespace std;

int zero_recursion(unordered_map<int,int>& zero_map, int n){
    if(zero_map.find(n) != zero_map.end()) {return zero_map[n];}
    
    zero_map[n] = zero_recursion(zero_map, n-1) + zero_recursion(zero_map, n-2);
    return zero_map[n];
}

int one_recursion(unordered_map<int,int>& one_map,int n){
    if(one_map.find(n) != one_map.end()) {return one_map[n];}
    
    one_map[n] = one_recursion(one_map, n-1) + one_recursion(one_map, n-2);
    return one_map[n];
}

int main(){
    int n;
    cin >> n;


    unordered_map<int, int> zero_map;
    zero_map[0] = 1;
    zero_map[1] = 0;
    unordered_map<int, int> one_map;
    one_map[0] = 0;
    one_map[1] = 1;
    for(int i = 0; i < n; i++){
        int num;
        cin >> num;
        zero_recursion(zero_map,num);
        one_recursion(one_map,num);
        cout << zero_map[num] << " " << one_map[num]<< endl;
    }
}