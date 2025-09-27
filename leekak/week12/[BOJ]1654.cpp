#include <iostream>
using namespace std;

int main() {
    int K, N;
    cin >> K >> N ;
    int cable[K];
    long start=1, end = 1;
    for(int i=0; i<K; i++) {
        cin >> cable[i];
        if(cable[i] > end) end = cable[i];
    }
    long result=1;
    while(start <= end) {
        long tmp = (start+end)/2;
        int sum = 0;
        for(int i=0; i<K; i++) {
            sum += cable[i]/tmp;
        }
        if(sum >= N) {
            result = max(result, tmp);
            start = tmp+1;
        }
        else {
            end = tmp-1;
        }
    }

    cout << result;
    return 0;
}
