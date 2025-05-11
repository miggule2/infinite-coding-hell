#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

void devide(vector<char>& str, int start, int length) {
    //base case
    //구간의 길이가 1이면 더 이상 공백으로 바꿀 수 없으니까 종료
    if(length == 1) return;
    //3등분 중에서 가운데를 공백으로 바꾸기
    for(int i=start+length/3; i<start+length/3+length/3; i++) {
        str[i] = ' ';
    }
    //3등분해서 재귀호출하기
    devide(str, start, length/3);
    devide(str, start + (length/3) *2, length/3);
}

int main() {
    int n;
				    while(cin>>n) {

        vector<char> cantor((int) pow(3, n), '-');
        devide(cantor, 0, cantor.size());

        for(int i=0; i<cantor.size(); i++) {
            cout << cantor[i];
        }
        cout << '\n';
    }
    return 0;
}

/*
 * base case : 모든 선의 길이가 1
 *
 * 왜 자꾸 25퍼에서 틀렸다노
 * 재귀로 풀면 안되나?
 *
 * 아니 들어봐
 * 처음에 while(!cin.eof()) 일케 하면서 풀었어
 * 근데 계속 백준에 넣으면 계속 25퍼에서 틀렸다는거야
 * 근데 아무리 생각해도 맞거든?
 * 그래서 while(cin>>n) 이렇게 바꿔봤다?
 * 그니까 맞았대;;;;;;
 * 저 두개 뭔 차인데?
 */
