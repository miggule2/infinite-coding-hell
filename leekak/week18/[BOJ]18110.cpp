#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    if(n==0) {
        cout << 0;
        return 0;
    }
    vector<int> vote;
    for(int i=0; i<n; i++) {
        int tmp;
        cin >> tmp;
        vote.push_back(tmp);
    }
    sort(vote.begin(), vote.end());
    int first, last;
    double m;
    m = floor((double)n*0.15 +0.5);
    first = (int)m;
    last = n-(int)m;
    double sum=0;
    for(int i=first; i<last; i++) {
        sum = sum + vote[i];
    }
    int result;
    result = floor((sum/(last - first))+0.5);
    cout << result;

    return 0;
}
