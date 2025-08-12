#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int N, Q;
    cin >> N >> Q;

    vector<int> tree(N+1);  // 땅의 점유 여부 저장 

    while(Q--) {
        int land, tmp;
        bool flag = false;  // 이미 점유된 땅 발견 여부
        cin >> land;
        tmp = land;

        stack<int> route;

        while(tmp!=0) {
            route.push(tmp);
            tmp = tmp/2;  // 부모 노드로 이동
        }
        while(!route.empty()) {
            tmp = route.top();
            if(tree[tmp]==1) {  // 이미 점유된 땅 발견
                cout << tmp << "\n";
                flag = true;
                break;
            } else {
                route.pop();
            }
        }
        // 경로 중 점유된 땅이 없는 경우
        if(!flag) {
            cout << 0 << "\n";
            tree[land] = 1;
        }
    }
    return 0;
}
