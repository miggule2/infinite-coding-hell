#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<int> arr(N);
    for(int i=0; i<N; i++) {
        cin >> arr[i];
    }
    int max = -(int)pow(10, 9);
    vector<int> maxi(N);
    int min_element=arr[0];
    for(int i=1; i<N; i++) {
        if(arr[i] < min_element) {
            min_element = arr[i];
        }
        if(max < (arr[i]-min_element)) {
            max = arr[i]-min_element;
        }
        maxi[i] = max;
    }
    for(int i=0; i<N; i++) {
        cout << maxi[i] << " ";
    }
    return 0;
}
