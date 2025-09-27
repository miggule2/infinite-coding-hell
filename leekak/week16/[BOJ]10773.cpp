#include <iostream>

using namespace std;
int main() {
    int K;
    cin >> K;
    int memory[K];
    int *ptr = memory;
    int sum=0;
    for(int i=0; i<K; i++) {
        int n;
        cin >> n;
        if(n == 0) {
            // 0이면 최근 숫자 제거
            ptr--;            // 포인터 한 칸 뒤로
            sum = sum - *ptr;
        } else {
            // 0이 아니면 스택에 push
            *ptr = n;          // 현재 위치에 저장
            sum = sum + *ptr;  // 합계에 더하기
            ptr++;             // stack top 이동
        }
    }
    cout << sum;
    return 0;
}
